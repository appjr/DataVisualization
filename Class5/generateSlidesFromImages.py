#!/usr/bin/env python3
"""
img2slide_master_style.py

Turn input images into consistent "slide images" by:
1) Stylizing the ORIGINAL image using a MASTER style image (content-preserving)
2) Adding a slide panel and optional title/subtitle overlay locally with Pillow

This avoids the common failure mode where the model ignores the original image.

Requires:
  pip install -U openai pillow

Usage:
  export OPENAI_API_KEY="..."

  # Single image
  python img2slide_master_style.py input.jpg --master master.png -o out.png \
      --title "Y-Axis Decisions" --subtitle "Should time series start at zero?"

  # Folder of images -> slides
  python img2slide_master_style.py ./imgs --master master.png --outdir ./slides_out \
      --title "My Deck" --subtitle "Stylized slides"

Notes:
- Uses GPT Image edit (multi-image): image[0]=content, image[1]=master style.
- Generates 1536x1024 (supported) then crops to 16:9 and resizes (default 1536x864).
- If you hit billing limits, the API will fail regardless of code.
"""

import os
import re
import glob
import base64
import argparse
from io import BytesIO
from typing import Tuple, Optional, List

from PIL import Image, ImageDraw, ImageFont
from openai import OpenAI


# -------------------------
# Utilities
# -------------------------
def is_image_file(path: str) -> bool:
    return path.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))


def safe_out_name(path: str) -> str:
    base = os.path.splitext(os.path.basename(path))[0]
    base = re.sub(r"[^a-zA-Z0-9_\-]+", "_", base).strip("_")
    return base or "slide"


def b64_to_pil(b64_json: str) -> Image.Image:
    return Image.open(BytesIO(base64.b64decode(b64_json))).convert("RGBA")


def crop_center_to_ratio(img: Image.Image, target_w: int, target_h: int) -> Image.Image:
    w, h = img.size
    target_ratio = target_w / target_h
    cur_ratio = w / h

    if cur_ratio > target_ratio:
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        return img.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        return img.crop((0, top, w, top + new_h))


def resize(img: Image.Image, size: Tuple[int, int]) -> Image.Image:
    return img.resize(size, Image.LANCZOS)


# -------------------------
# Slide panel + text overlay
# -------------------------
def load_font(preferred_paths: List[str], size: int) -> ImageFont.ImageFont:
    for p in preferred_paths:
        try:
            return ImageFont.truetype(p, size=size)
        except Exception:
            continue
    return ImageFont.load_default()


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> List[str]:
    words = text.split()
    if not words:
        return []
    lines, cur = [], []
    for w in words:
        test = " ".join(cur + [w]).strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width:
            cur.append(w)
        else:
            if cur:
                lines.append(" ".join(cur))
            cur = [w]
    if cur:
        lines.append(" ".join(cur))
    return lines


def add_blank_board(
    img: Image.Image,
    box_rel=(0.22, 0.14, 0.92, 0.62),  # left, top, right, bottom (relative to W,H)
    alpha: int = 170,
    outline_alpha: int = 70,
    radius: int = 40,
    outline_width: int = 4,
) -> Image.Image:
    """
    Adds a translucent rounded-rectangle "board" panel without removing underlying content.
    """
    out = img.convert("RGBA")
    W, H = out.size
    l = int(W * box_rel[0]); t = int(H * box_rel[1])
    r = int(W * box_rel[2]); b = int(H * box_rel[3])

    overlay = Image.new("RGBA", out.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    d.rounded_rectangle(
        [l, t, r, b],
        radius=radius,
        fill=(255, 255, 255, alpha),
        outline=(0, 0, 0, outline_alpha),
        width=outline_width,
    )
    return Image.alpha_composite(out, overlay)


def overlay_title_subtitle(
    img: Image.Image,
    title: Optional[str],
    subtitle: Optional[str],
    margin: int = 96,
) -> Image.Image:
    if not (title or subtitle):
        return img

    out = img.convert("RGBA")
    W, H = out.size
    draw = ImageDraw.Draw(out)

    title_font = load_font(
        ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
         "/Library/Fonts/Arial Bold.ttf",
         "C:\\Windows\\Fonts\\arialbd.ttf"],
        72
    )
    subtitle_font = load_font(
        ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf",
         "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
         "/Library/Fonts/Arial Italic.ttf",
         "C:\\Windows\\Fonts\\ariali.ttf"],
        44
    )

    x0 = margin
    y = margin
    text_w = W - 2 * margin
    title_color = (25, 35, 45, 255)
    subtitle_color = (45, 65, 85, 255)

    if title:
        for line in wrap_text(draw, title, title_font, text_w):
            draw.text((x0, y), line, font=title_font, fill=title_color)
            y += int(title_font.size * 1.15)
        y += 10

    if subtitle:
        for line in wrap_text(draw, subtitle, subtitle_font, text_w):
            draw.text((x0, y), line, font=subtitle_font, fill=subtitle_color)
            y += int(subtitle_font.size * 1.25)

    return out


# -------------------------
# Model transform (content-preserving)
# -------------------------
def build_prompt(preserve_hint: str = "") -> str:
    base = """
IMAGE ORDER:
- Image #1 (first) is the CONTENT image to preserve.
- Image #2 (second) is the MASTER STYLE image to match.

TASK:
Create a stylized 2D retro cartoon version of Image #1 in the exact style of Image #2.

PRESERVATION RULES (VERY IMPORTANT):
- Keep the main subject(s) from Image #1 clearly recognizable.
- Preserve overall composition, camera angle, and relative positions.
- Do NOT replace the subject with different people/objects.
- Only stylize (outlines, palette, grain, simplified shading).

SLIDE RULES:
- NO TEXT / WORDS / LETTERS / NUMBERS anywhere.
- Keep background simplified; do not add unrelated characters.
""".strip()

    preserve_hint = preserve_hint.strip()
    if preserve_hint:
        base += "\n\nPreserve these key elements from Image #1:\n" + preserve_hint
    return base


def transform_to_master_style(
    client: OpenAI,
    content_path: str,
    master_path: str,
    model: str = "chatgpt-image-latest",
    gen_size: str = "1536x1024",
    quality: str = "high",
    preserve_hint: str = "",
) -> Image.Image:
    """
    Multi-image edit:
      image[0] = content photo/image (preserve)
      image[1] = master style anchor
    """
    prompt = build_prompt(preserve_hint)

    with open(content_path, "rb") as f_content, open(master_path, "rb") as f_master:
        res = client.images.edit(
            model=model,
            image=[f_content, f_master],
            prompt=prompt,
            size=gen_size,
            quality=quality,
        )

    return b64_to_pil(res.data[0].b64_json)
    


# -------------------------
# Pipeline
# -------------------------
def process_one(
    client: OpenAI,
    content_path: str,
    master_path: str,
    out_path: str,
    out_size: Tuple[int, int],
    model: str,
    gen_size: str,
    quality: str,
    add_panel: bool,
    panel_box_rel: Tuple[float, float, float, float],
    panel_alpha: int,
    title: Optional[str],
    subtitle: Optional[str],
    preserve_hint: str,
):
    # 1) stylize while preserving content
    img = transform_to_master_style(
        client=client,
        content_path=content_path,
        master_path=master_path,
        model=model,
        gen_size=gen_size,
        quality=quality,
        preserve_hint=preserve_hint,
    )

    # 2) crop to 16:9 and resize
    img = crop_center_to_ratio(img, out_size[0], out_size[1])
    img = resize(img, out_size)

    # 3) add panel + overlay text locally (so model never needs to create text)
    if add_panel:
        img = add_blank_board(img, box_rel=panel_box_rel, alpha=panel_alpha)

    img = overlay_title_subtitle(img, title, subtitle)

    img.save(out_path)
    print(f"Saved: {out_path}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="Image file OR directory of images")
    ap.add_argument("--master", required=True, help="Master style image (png/jpg/webp)")
    ap.add_argument("--model", default="chatgpt-image-latest",
                    choices=["chatgpt-image-latest", "gpt-image-1", "gpt-image-1-mini", "chatgpt-image-latest"])
    ap.add_argument("--gen-size", default="1536x1024",
                    choices=["1024x1024", "1536x1024", "1024x1536", "auto"],
                    help="Generation size (supported by GPT Image)")
    ap.add_argument("--quality", default="high", choices=["low", "medium", "high"])
    ap.add_argument("--width", type=int, default=1536)
    ap.add_argument("--height", type=int, default=864)

    ap.add_argument("-o", "--output", help="Output file (single input only)")
    ap.add_argument("--outdir", help="Output directory (required for directory input)")

    ap.add_argument("--panel", action="store_true", help="Add a translucent slide panel")
    ap.add_argument("--panel-alpha", type=int, default=170, help="Panel opacity 0-255")
    ap.add_argument("--panel-box", default="0.22,0.14,0.92,0.62",
                    help="Panel box as rel coords left,top,right,bottom (0..1), e.g. 0.22,0.14,0.92,0.62")

    ap.add_argument("--title", default=None)
    ap.add_argument("--subtitle", default=None)

    ap.add_argument("--preserve-hint", default="",
                    help='Optional short hint of what to preserve, e.g. "two women, tablet, cafe table, coffee cup"')

    args = ap.parse_args()

    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("Missing OPENAI_API_KEY environment variable.")
    if not os.path.exists(args.master):
        raise SystemExit(f"Master image not found: {args.master}")

    # Parse panel box
    try:
        parts = [float(x.strip()) for x in args.panel_box.split(",")]
        if len(parts) != 4:
            raise ValueError
        panel_box_rel = (parts[0], parts[1], parts[2], parts[3])
    except Exception:
        raise SystemExit("Invalid --panel-box. Use: left,top,right,bottom (four floats).")

    client = OpenAI()
    out_size = (args.width, args.height)

    # Directory mode
    if os.path.isdir(args.input):
        if not args.outdir:
            raise SystemExit("For directory input, please provide --outdir.")
        os.makedirs(args.outdir, exist_ok=True)
        files = [p for p in sorted(glob.glob(os.path.join(args.input, "*"))) if is_image_file(p)]
        if not files:
            raise SystemExit("No images found in input directory.")

        for p in files:
            out_path = os.path.join(args.outdir, f"{safe_out_name(p)}.png")
            process_one(
                client=client,
                content_path=p,
                master_path=args.master,
                out_path=out_path,
                out_size=out_size,
                model=args.model,
                gen_size=args.gen_size,
                quality=args.quality,
                add_panel=args.panel,
                panel_box_rel=panel_box_rel,
                panel_alpha=args.panel_alpha,
                title=args.title,
                subtitle=args.subtitle,
                preserve_hint=args.preserve_hint,
            )
        return

    # Single file mode
    if not os.path.exists(args.input) or not is_image_file(args.input):
        raise SystemExit("Input must be an existing image file (.png/.jpg/.jpeg/.webp) or a directory.")

    if args.output:
        out_path = args.output
    elif args.outdir:
        os.makedirs(args.outdir, exist_ok=True)
        out_path = os.path.join(args.outdir, f"{safe_out_name(args.input)}.png")
    else:
        out_path = os.path.splitext(args.input)[0] + "_slide.png"

    process_one(
        client=client,
        content_path=args.input,
        master_path=args.master,
        out_path=out_path,
        out_size=out_size,
        model=args.model,
        gen_size=args.gen_size,
        quality=args.quality,
        add_panel=args.panel,
        panel_box_rel=panel_box_rel,
        panel_alpha=args.panel_alpha,
        title=args.title,
        subtitle=args.subtitle,
        preserve_hint=args.preserve_hint
    )


if __name__ == "__main__":
    main()
