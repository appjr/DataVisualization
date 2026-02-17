#!/usr/bin/env python3
"""
md2cartoon_slides.py

Generate slide PNGs from Markdown using a MASTER reference image as a style anchor.
- Uses GPT Image edits endpoint with multipart image[] input (supports gpt-image-1 / 1.5 / mini)
- Generates NO TEXT in the background; overlays crisp text with Pillow
- Outputs 16:9 PNGs (default 1536x864) by cropping from a supported GPT Image size (1536x1024)

Install:
  pip install -U openai pillow markdown-it-py

Run:
  export OPENAI_API_KEY="..."
  python md2cartoon_slides.py input.md --master master.png -o out.png
  python md2cartoon_slides.py slides_dir/ --master master.png --outdir out_slides
"""

import os
import re
import glob
import base64
import argparse
from dataclasses import dataclass, field
from io import BytesIO
from typing import List, Tuple, Optional

from markdown_it import MarkdownIt
from PIL import Image, ImageDraw, ImageFont

from openai import OpenAI


# -----------------------
# Markdown parsing
# -----------------------
@dataclass
class SlideContent:
    title: str = ""
    subtitle: str = ""
    bullets: List[str] = field(default_factory=list)


def parse_markdown_to_slide(md_text: str) -> SlideContent:
    md = MarkdownIt()
    tokens = md.parse(md_text)

    slide = SlideContent()
    got_title = False
    got_subtitle = False

    i = 0
    while i < len(tokens):
        t = tokens[i]

        # headings
        if t.type == "heading_open":
            level = int(t.tag[1])
            if i + 1 < len(tokens) and tokens[i + 1].type == "inline":
                txt = tokens[i + 1].content.strip()
                if level == 1 and not got_title:
                    slide.title, got_title = txt, True
                elif level == 2 and not got_subtitle:
                    slide.subtitle, got_subtitle = txt, True
            i += 1

        # list items
        if t.type == "list_item_open":
            j = i + 1
            li = ""
            while j < len(tokens) and tokens[j].type != "list_item_close":
                if tokens[j].type == "inline":
                    li += tokens[j].content
                j += 1
            li = re.sub(r"\s+", " ", li).strip()
            if li:
                slide.bullets.append(li)
            i = j

        i += 1

    # fallback title
    if not slide.title:
        for line in md_text.splitlines():
            s = line.strip()
            if s:
                slide.title = re.sub(r"^#+\s*", "", s)
                break

    # fallback subtitle: italic-only line like *...* or _..._
    if not slide.subtitle:
        for line in md_text.splitlines():
            s = line.strip()
            m = re.fullmatch(r"[*_](.+)[*_]", s)
            if m:
                slide.subtitle = m.group(1).strip()
                break

    return slide


# -----------------------
# Image helpers
# -----------------------
def b64_to_pil(b64_json: str) -> Image.Image:
    img_bytes = base64.b64decode(b64_json)
    return Image.open(BytesIO(img_bytes)).convert("RGBA")


def crop_center_to_ratio(img: Image.Image, target_w: int, target_h: int) -> Image.Image:
    w, h = img.size
    target_ratio = target_w / target_h
    cur_ratio = w / h

    if cur_ratio > target_ratio:
        # too wide, crop width
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        return img.crop((left, 0, left + new_w, h))
    else:
        # too tall, crop height
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        return img.crop((0, top, w, top + new_h))


def resize(img: Image.Image, size: Tuple[int, int]) -> Image.Image:
    return img.resize(size, Image.LANCZOS)


# -----------------------
# Text rendering
# -----------------------
def load_font(preferred: List[str], size: int) -> ImageFont.ImageFont:
    for p in preferred:
        try:
            return ImageFont.truetype(p, size=size)
        except Exception:
            pass
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


def draw_slide_text(img: Image.Image, slide: SlideContent, margin: int = 96, panel_alpha: int = 170) -> Image.Image:
    W, H = img.size
    out = img.copy()

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
    body_font = load_font(
        ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
         "/Library/Fonts/Arial.ttf",
         "C:\\Windows\\Fonts\\arial.ttf"],
        40
    )

    x0, y = margin, margin
    text_w = W - 2 * margin

    # translucent panel for readability
    panel = Image.new("RGBA", out.size, (0, 0, 0, 0))
    pdraw = ImageDraw.Draw(panel)
    pdraw.rounded_rectangle(
        [x0 - 32, y - 32, x0 + text_w + 32, H - margin + 32],
        radius=36,
        fill=(255, 255, 255, panel_alpha),
        outline=(0, 0, 0, 60),
        width=3
    )
    out = Image.alpha_composite(out, panel)
    draw = ImageDraw.Draw(out)

    title_color = (25, 35, 45, 255)
    subtitle_color = (45, 65, 85, 255)
    body_color = (25, 35, 45, 255)

    # title
    for line in wrap_text(draw, slide.title, title_font, text_w):
        draw.text((x0, y), line, font=title_font, fill=title_color)
        y += int(title_font.size * 1.15)
    y += 8

    # subtitle
    if slide.subtitle:
        for line in wrap_text(draw, slide.subtitle, subtitle_font, text_w):
            draw.text((x0, y), line, font=subtitle_font, fill=subtitle_color)
            y += int(subtitle_font.size * 1.25)
        y += 18

    # bullets
    bullet_indent, bullet_gap = 44, 14
    for b in slide.bullets:
        lines = wrap_text(draw, b, body_font, text_w - bullet_indent)
        if not lines:
            continue
        draw.text((x0, y), "•", font=body_font, fill=body_color)
        draw.text((x0 + bullet_indent, y), lines[0], font=body_font, fill=body_color)
        y += int(body_font.size * 1.3)
        for cont in lines[1:]:
            draw.text((x0 + bullet_indent, y), cont, font=body_font, fill=body_color)
            y += int(body_font.size * 1.3)
        y += bullet_gap

    return out


# -----------------------
# GPT Image reference edit (correct call shape)
# -----------------------
def build_hint(slide: SlideContent) -> str:
    parts = [slide.title]
    if slide.subtitle:
        parts.append(slide.subtitle)
    if slide.bullets:
        parts.append("; ".join(slide.bullets[:3]))
    return re.sub(r"\s+", " ", " | ".join([p for p in parts if p]).strip())[:240]


def build_prompt(hint: str) -> str:
    return f"""
STRICT STYLE MATCH.
Use the reference image as the style anchor (same palette, line weight, texture, character proportions).

Create a NEW 16:9 slide background variation for:
{hint}

Rules:
- NO TEXT / LETTERS / WORDS / NUMBERS anywhere.
- Leave a large clean central “board/panel” area for text overlay.
- Keep a friendly professor/scientist character off to one side.
- Add a few simple props relevant to the topic (chart/clock/calendar), uncluttered.
""".strip()


def generate_background_from_master(
    client: OpenAI,
    master_path: str,
    hint: str,
    model: str = "gpt-image-1",   # best quality; switch to "gpt-image-1" if you want
    size: str = "1536x1024",
    quality: str = "high",
) -> Image.Image:
    # IMPORTANT: pass a file handle inside a LIST => multipart image[]
    with open(master_path, "rb") as master_file:
        result = client.images.edit(
            model=model,
            image=[master_file],     # <-- this is the key fix
            prompt=build_prompt(hint),
            size=size,
            quality=quality,
        )
    return b64_to_pil(result.data[0].b64_json)


# -----------------------
# Main slide creation
# -----------------------
def make_slide_png(
    client: OpenAI,
    md_text: str,
    master_path: str,
    out_size: Tuple[int, int] = (1536, 864),
    model: str = "gpt-image-1.5",
) -> Image.Image:
    slide = parse_markdown_to_slide(md_text)
    hint = build_hint(slide)

    bg = generate_background_from_master(
        client=client,
        master_path=master_path,
        hint=hint,
        model=model,
        size="1536x1024",   # supported for GPT Image edits
        quality="high",
    )

    # Crop to 16:9 then resize to final output
    bg = crop_center_to_ratio(bg, out_size[0], out_size[1])
    bg = resize(bg, out_size)

    final_img = draw_slide_text(bg, slide)
    return final_img


# -----------------------
# CLI / IO
# -----------------------
def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def safe_basename(path: str) -> str:
    base = os.path.splitext(os.path.basename(path))[0]
    base = re.sub(r"[^a-zA-Z0-9_\-]+", "_", base).strip("_")
    return base or "slide"


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="Input .md file OR directory of .md files")
    ap.add_argument("--master", required=True, help="Master reference image (png/jpg/webp)")
    ap.add_argument("-o", "--output", help="Output PNG path (single input file only)")
    ap.add_argument("--outdir", help="Output directory (for directory input)")
    ap.add_argument("--width", type=int, default=1536)
    ap.add_argument("--height", type=int, default=864)
    ap.add_argument("--model", default="gpt-image-1.5",
                    choices=["gpt-image-1.5", "gpt-image-1", "gpt-image-1-mini", "chatgpt-image-latest"],
                    help="GPT Image model to use")
    args = ap.parse_args()

    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("Missing OPENAI_API_KEY")

    if not os.path.exists(args.master):
        raise SystemExit(f"Master image not found: {args.master}")

    client = OpenAI()
    out_size = (args.width, args.height)

    # Directory input
    if os.path.isdir(args.input):
        if not args.outdir:
            raise SystemExit("For directory input, provide --outdir")
        ensure_dir(args.outdir)
        md_files = sorted(glob.glob(os.path.join(args.input, "*.md")))
        if not md_files:
            raise SystemExit("No .md files found in input directory")
        for md_path in md_files:
            img = make_slide_png(client, read_text(md_path), args.master, out_size=out_size, model=args.model)
            out_path = os.path.join(args.outdir, f"{safe_basename(md_path)}.png")
            img.save(out_path)
            print(f"Saved: {out_path}")
        return

    # Single file input
    if not os.path.exists(args.input):
        raise SystemExit(f"Input not found: {args.input}")

    if args.output:
        out_path = args.output
    elif args.outdir:
        ensure_dir(args.outdir)
        out_path = os.path.join(args.outdir, f"{safe_basename(args.input)}.png")
    else:
        out_path = os.path.splitext(args.input)[0] + ".png"

    img = make_slide_png(client, read_text(args.input), args.master, out_size=out_size, model=args.model)
    img.save(out_path)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
