"""Generate a single slide image using the OpenAI Images API.

This script is for *one slide at a time* so you can iterate on prompt/style.

Prereq:
  export OPENAI_API_KEY="..."

Example:
  python Class4/generate_cartoon_slide_openai.py --slide 1 --style retro60s
"""

from __future__ import annotations

import argparse
import base64
import importlib.util
import io
import os
import subprocess
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import List

import requests
from PIL import Image, ImageDraw, ImageFont


BASE_DIR = Path(__file__).resolve().parent
MD_FILE = BASE_DIR / "Class4.md"
OUT_DIR = BASE_DIR / "openai_cartoon_slides"

# macOS Keychain settings
# We'll look for a *generic password* with this service name.
KEYCHAIN_SERVICE = "openai-api-key"


def load_openai_key_from_keychain(service: str) -> str:
    """Read OpenAI API key from macOS Keychain.

    Expects a generic password item:
      account = your username ("$USER")
      service = KEYCHAIN_SERVICE (default: "openai-api-key")

    Returns empty string if not found.
    """

    user = os.getenv("USER", "")
    if not user:
        return ""

    # -w: print password only
    cmd = ["security", "find-generic-password", "-a", user, "-s", service, "-w"]
    try:
        proc = subprocess.run(cmd, check=False, capture_output=True, text=True)
    except FileNotFoundError:
        # Not macOS or security tool unavailable
        return ""

    if proc.returncode != 0:
        return ""

    return (proc.stdout or "").strip()


def _load_helpers():
    """Load helper functions from create_slide_images.py (no package install needed)."""
    helpers_path = BASE_DIR / "create_slide_images.py"
    spec = importlib.util.spec_from_file_location("class4_helpers", helpers_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not import helpers from {helpers_path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_helpers = _load_helpers()
split_markdown_slides = _helpers.split_markdown_slides
extract_title_and_points = _helpers.extract_title_and_points
detect_theme = _helpers.detect_theme


@dataclass(frozen=True)
class SlideSpec:
    slide_num: int
    title: str
    bullets: List[str]
    theme: str


def get_slide_spec(slide_num: int) -> SlideSpec:
    if not MD_FILE.exists():
        raise FileNotFoundError(f"Missing markdown file: {MD_FILE}")

    slides = split_markdown_slides(MD_FILE.read_text(encoding="utf-8"))
    if not (1 <= slide_num <= len(slides)):
        raise ValueError(f"Slide {slide_num} is out of range (1..{len(slides)})")

    slide_text = slides[slide_num - 1]
    title, bullets = extract_title_and_points(slide_text)
    theme = detect_theme(title, bullets, slide_text)
    return SlideSpec(slide_num=slide_num, title=title, bullets=bullets, theme=theme)


def build_background_prompt(spec: SlideSpec, style: str) -> str:
    """Prompt for a background illustration with room for text overlay."""
    # Avoid model-generated garbled typography.
    base = (
        "Create a single 16:9 background illustration. "
        "NO TEXT, NO LETTERS, NO WORDS, NO LOGOS. "
        "Cartoon illustration with bold outlines and clean cel shading. "
        "Bright but tasteful pastel palette, crisp shapes. "
        "Leave a clear empty area on the LEFT side for a dark translucent text panel overlay. "
    )

    if style == "retro60s":
        vibe = (
            "Retro-futuristic 1960s space-age city scene: floating buildings on stilts, "
            "monorail arc, bubble domes, sleek flying cars, starry gradient sky; optimistic vibe. "
        )
    else:
        vibe = "Friendly modern cartoon background with subtle data visualization motifs. "

    theme_hint = {
        "workflow": "Include a subtle flow-diagram/holographic panel motif.",
        "distribution": "Include subtle holographic histogram bars and a smooth density curve.",
        "correlation": "Include a subtle heatmap grid/matrix motif.",
        "missing": "Include a subtle grid motif with a few missing squares/gaps.",
        "outlier": "Include a subtle scatter-plot motif with a couple highlighted outliers.",
        "comparison": "Include subtle split panels and grouped bars.",
        "exercise": "Include subtle checklist cards and mini chart tiles.",
        "code": "Include subtle terminal/code panels (still NO readable text).",
    }.get(spec.theme, "Include subtle chart and magnifying-glass motifs.")

    return base + vibe + theme_hint


def openai_generate_background(prompt: str, size: str, api_key: str) -> Image.Image:
    url = "https://api.openai.com/v1/images/generations"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "gpt-image-1",
        "prompt": prompt,
        "size": size,
    }
    resp = requests.post(url, headers=headers, json=payload, timeout=180)
    if resp.status_code >= 300:
        raise RuntimeError(f"OpenAI Images API error {resp.status_code}: {resp.text}")

    data = resp.json()
    try:
        item = data["data"][0]
    except Exception as e:
        raise RuntimeError(f"Unexpected OpenAI response shape: {data}") from e

    # Prefer inline base64 when available
    if isinstance(item, dict) and item.get("b64_json"):
        img_bytes = base64.b64decode(item["b64_json"])
        return Image.open(io.BytesIO(img_bytes)).convert("RGB")

    # Otherwise, fall back to URL-based response
    if isinstance(item, dict) and item.get("url"):
        r = requests.get(item["url"], timeout=180)
        if r.status_code >= 300:
            raise RuntimeError(f"Failed to download image from url (HTTP {r.status_code})")
        return Image.open(io.BytesIO(r.content)).convert("RGB")

    raise RuntimeError(f"OpenAI response missing image content (expected b64_json or url): {data}")


def pick_font(size: int, bold: bool = False):
    """Best-effort font selection (macOS), fallback to default."""
    candidates = []
    if bold:
        candidates += [
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "/Library/Fonts/Arial Bold.ttf",
        ]
    candidates += [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for p in candidates:
        try:
            if Path(p).exists():
                return ImageFont.truetype(p, size=size)
        except Exception:
            pass
    return ImageFont.load_default()


def overlay_slide_text(bg: Image.Image, spec: SlideSpec) -> Image.Image:
    bg = bg.convert("RGBA")
    w, h = bg.size

    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)

    # Panel geometry
    pad = int(w * 0.05)
    x0 = pad
    y0 = int(h * 0.16)
    x1 = int(w * 0.57)
    y1 = int(h * 0.80)
    radius = int(min(w, h) * 0.02)

    d.rounded_rectangle(
        [x0, y0, x1, y1],
        radius=radius,
        fill=(10, 18, 44, 175),
        outline=(160, 245, 255, 255),
        width=4,
    )

    title_font = pick_font(int(h * 0.056), bold=True)
    body_font = pick_font(int(h * 0.034), bold=False)
    small_font = pick_font(int(h * 0.028), bold=False)

    tx = x0 + int(w * 0.03)
    ty = y0 + int(h * 0.03)
    d.text((tx, ty), f"Slide {spec.slide_num:02d}", fill=(160, 245, 255, 255), font=small_font)
    ty += int(h * 0.048)

    for line in textwrap.wrap(spec.title.strip(), width=28)[:2]:
        d.text((tx, ty), line, fill=(245, 254, 255, 255), font=title_font)
        ty += int(h * 0.066)
    ty += int(h * 0.01)

    bullets = [b.strip() for b in spec.bullets if b.strip()]
    bullets = bullets[:4] or ["(No bullets detected on this slide)"]
    for b in bullets:
        b = " ".join(b.split())
        for line in textwrap.wrap(f"• {b}", width=44)[:2]:
            d.text((tx, ty), line, fill=(220, 252, 255, 255), font=body_font)
            ty += int(h * 0.045)
        ty += int(h * 0.010)

    return Image.alpha_composite(bg, overlay).convert("RGB")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a single cartoon slide image with OpenAI")
    parser.add_argument("--slide", type=int, default=1, help="1-based slide number")
    parser.add_argument("--style", choices=["retro60s", "flat"], default="retro60s")
    parser.add_argument("--size", default="1792x1024", help="OpenAI image size (e.g., 1024x1024, 1792x1024)")
    parser.add_argument("--out-dir", default=str(OUT_DIR))
    parser.add_argument("--no-overlay", action="store_true", help="Only save background (no title/bullets overlay)")
    args = parser.parse_args()

    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        # Fall back to macOS Keychain
        api_key = load_openai_key_from_keychain(service=KEYCHAIN_SERVICE)
    if not api_key:
        raise RuntimeError(
            "OpenAI API key not found. Set OPENAI_API_KEY or store it in macOS Keychain.\n\n"
            "To store in Keychain (recommended), run:\n"
            f"  security add-generic-password -a \"$USER\" -s \"{KEYCHAIN_SERVICE}\" -w \"YOUR_KEY\" -U\n"
        )

    spec = get_slide_spec(args.slide)
    prompt = build_background_prompt(spec, style=args.style)

    bg = openai_generate_background(prompt=prompt, size=args.size, api_key=api_key)

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    bg_path = out_dir / f"slide_{spec.slide_num:03d}_bg.png"
    bg.save(bg_path)

    if args.no_overlay:
        print(f"Created (background): {bg_path}")
        return

    final = overlay_slide_text(bg, spec)
    out_path = out_dir / f"slide_{spec.slide_num:03d}.png"
    final.save(out_path)
    print(f"Created: {out_path}")
    print(f"Background saved: {bg_path}")


if __name__ == "__main__":
    main()
