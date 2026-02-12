"""Class 4 – Render a single slide as a cartoon-style PNG.

This is intentionally *single-slide* oriented (no PPTX output), so you can
iterate on style quickly before batch-rendering all slides.

Usage:
  python Class4/render_cartoon_slide.py --slide 1 --style flat

Outputs:
  Class4/cartoon_slides/slide_001_flat.png (by default)
"""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path
from typing import List

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch


BASE_DIR = Path(__file__).resolve().parent
MD_FILE = BASE_DIR / "Class4.md"
DEFAULT_OUT_DIR = BASE_DIR / "cartoon_slides"


def _load_slide_helpers():
    """Load helpers from create_slide_images.py without requiring a package import."""
    helpers_path = BASE_DIR / "create_slide_images.py"
    spec = importlib.util.spec_from_file_location("class4_slide_helpers", helpers_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not import helpers from {helpers_path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_helpers = _load_slide_helpers()

split_markdown_slides = _helpers.split_markdown_slides
extract_title_and_points = _helpers.extract_title_and_points
detect_theme = _helpers.detect_theme
create_jetsons_slide_image = _helpers.create_jetsons_slide_image


def _soft_gradient_background(ax) -> None:
    """Light, friendly background (flat-cartoon vibe)."""
    h, w = 700, 950
    y = np.linspace(0, 1, h).reshape(-1, 1)
    top = np.array([0.97, 0.99, 1.00])      # near-white blue
    bottom = np.array([0.84, 0.95, 1.00])   # soft sky
    grad = top * (1 - y) + bottom * y
    grad = np.repeat(grad[:, None, :], w, axis=1)
    ax.imshow(grad, extent=[0, 10, 0, 7.5], aspect="auto", zorder=0)


def _cloud(ax, x: float, y: float, s: float, z: int = 2) -> None:
    col = "#ffffff"
    edge = "#cfe6ff"
    for dx, dy, r in [(0.0, 0.0, 0.35), (0.35, 0.08, 0.28), (-0.32, 0.06, 0.26), (0.12, 0.18, 0.22)]:
        ax.add_patch(Circle((x + dx * s, y + dy * s), r * s, facecolor=col, edgecolor=edge, linewidth=2, zorder=z))
    ax.add_patch(
        FancyBboxPatch(
            (x - 0.62 * s, y - 0.22 * s),
            1.28 * s,
            0.42 * s,
            boxstyle="round,pad=0.02,rounding_size=0.2",
            facecolor=col,
            edgecolor=edge,
            linewidth=2,
            zorder=z,
        )
    )


def _desk_scene(ax, rng: np.random.Generator) -> None:
    """Simple desk + card layout; keeps it clean and "cartoony"."""
    # desk
    ax.add_patch(Rectangle((0, 0), 10, 1.35, facecolor="#ffdfb8", edgecolor="#e9b27b", linewidth=2.5, zorder=3))
    ax.add_patch(Rectangle((0, 1.25), 10, 0.10, facecolor="#ffd6a0", edgecolor="none", zorder=4))

    # a monitor stand
    ax.add_patch(FancyBboxPatch((6.8, 1.05), 1.7, 0.3, boxstyle="round,pad=0.02,rounding_size=0.08",
                               facecolor="#7bd3ff", edgecolor="#2b7db3", linewidth=2.2, zorder=5))

    # a sticky note
    ax.add_patch(FancyBboxPatch((1.0, 0.55), 1.35, 0.85, boxstyle="round,pad=0.03,rounding_size=0.08",
                               facecolor="#fff3a6", edgecolor="#e0c75a", linewidth=2, zorder=6))
    ax.text(1.15, 1.15, "EDA", fontsize=14, fontweight="bold", color="#6b5b00", zorder=7)
    ax.plot([1.15, 2.2], [1.02, 1.02], color="#6b5b00", linewidth=2, zorder=7)

    # small mug
    ax.add_patch(FancyBboxPatch((2.7, 0.48), 0.55, 0.62, boxstyle="round,pad=0.02,rounding_size=0.12",
                               facecolor="#ffffff", edgecolor="#9ac4e8", linewidth=2, zorder=6))
    ax.add_patch(Circle((3.26, 0.78), 0.17, facecolor="none", edgecolor="#9ac4e8", linewidth=2, zorder=6))
    ax.add_patch(Rectangle((2.78, 0.92), 0.40, 0.08, facecolor="#ff9bb3", edgecolor="none", zorder=7, alpha=0.9))

    # a playful paper sheet with mini chart
    ax.add_patch(FancyBboxPatch((4.0, 0.55), 1.7, 0.95, boxstyle="round,pad=0.02,rounding_size=0.06",
                               facecolor="#ffffff", edgecolor="#9ac4e8", linewidth=2, zorder=6))
    xs = np.linspace(4.2, 5.5, 7)
    ys = 0.75 + rng.uniform(0.05, 0.65, size=len(xs))
    ax.plot(xs, ys, color="#2b7db3", linewidth=2.2, zorder=7)
    ax.scatter(xs, ys, s=18, color="#ff6b8f", zorder=8)


def _icon_magnifying_glass(ax, x: float, y: float, s: float) -> None:
    ax.add_patch(Circle((x, y), 0.42 * s, facecolor="#ffffff", edgecolor="#2b7db3", linewidth=3, zorder=8))
    ax.add_patch(Circle((x, y), 0.30 * s, facecolor="#dff1ff", edgecolor="none", zorder=8, alpha=0.9))
    ax.add_patch(
        FancyBboxPatch(
            (x + 0.30 * s, y - 0.55 * s),
            0.18 * s,
            0.62 * s,
            boxstyle="round,pad=0.02,rounding_size=0.09",
            facecolor="#ff6b8f",
            edgecolor="#b33856",
            linewidth=2.5,
            zorder=8,
        )
    )


def _icon_chart_card(ax, x: float, y: float, w: float, h: float, rng: np.random.Generator) -> None:
    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.03,rounding_size=0.12",
            facecolor="#ffffff",
            edgecolor="#9ac4e8",
            linewidth=2.5,
            zorder=7,
        )
    )
    # bars
    n = 6
    bw = w / (n + 1)
    for i in range(n):
        bh = float(rng.uniform(0.2, 0.85) * (h - 0.35))
        ax.add_patch(Rectangle((x + 0.15 + i * bw, y + 0.18), bw * 0.6, bh, facecolor="#7bd3ff", edgecolor="#2b7db3", linewidth=1.6, zorder=8))
    # title line
    ax.plot([x + 0.18, x + w - 0.18], [y + h - 0.22, y + h - 0.22], color="#cfe6ff", linewidth=3, zorder=8)


def create_flat_cartoon_slide_image(
    slide_num: int,
    title: str,
    bullets: List[str],
    slide_text: str,
    out_path: Path,
) -> None:
    """Render a single slide as a clean, generic flat-cartoon image."""
    rng = np.random.default_rng(slide_num * 2029 + len(title) * 97)

    fig, ax = plt.subplots(figsize=(10, 7.5), dpi=180)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    _soft_gradient_background(ax)

    # clouds / abstract blobs
    _cloud(ax, 2.0, 6.7, 1.0)
    _cloud(ax, 7.7, 6.9, 0.9)
    ax.add_patch(Circle((8.9, 5.6), 0.75, facecolor="#ffd6a0", edgecolor="#f2a65a", linewidth=2.5, zorder=1, alpha=0.95))

    _desk_scene(ax, rng)

    theme = detect_theme(title, bullets, slide_text)

    # Main title card
    ax.add_patch(
        FancyBboxPatch(
            (0.7, 5.25),
            8.6,
            1.6,
            boxstyle="round,pad=0.05,rounding_size=0.2",
            facecolor="#ffffff",
            edgecolor="#9ac4e8",
            linewidth=3,
            zorder=9,
        )
    )
    ax.text(1.0, 6.55, f"Slide {slide_num:02d}", fontsize=11, color="#2b7db3", fontweight="bold", zorder=10)
    ax.text(1.0, 6.15, title, fontsize=22, color="#1b3552", fontweight="bold", zorder=10)
    ax.text(1.0, 5.75, "Cartoon-style slide image", fontsize=10.5, color="#58708a", zorder=10)

    # Content area
    ax.add_patch(
        FancyBboxPatch(
            (0.7, 1.6),
            5.0,
            3.4,
            boxstyle="round,pad=0.05,rounding_size=0.18",
            facecolor="#ffffff",
            edgecolor="#cfe6ff",
            linewidth=2.5,
            zorder=8,
        )
    )
    ax.text(0.95, 4.75, "Key points", fontsize=12, fontweight="bold", color="#2b7db3", zorder=10)

    y = 4.35
    shown = bullets[:4] if bullets else []
    for b in shown:
        txt = " ".join(b.split())
        if len(txt) > 72:
            txt = txt[:69] + "..."
        ax.text(1.0, y, f"• {txt}", fontsize=10.2, color="#1b3552", zorder=10)
        y -= 0.42
    if not shown:
        ax.text(1.0, y, "• (No bullets detected — using title slide)", fontsize=10.2, color="#58708a", zorder=10)

    # Right-side illustration cards (based on theme)
    ax.text(6.0, 4.85, f"Theme: {theme}", fontsize=11, fontweight="bold", color="#2b7db3", zorder=10)

    _icon_magnifying_glass(ax, 6.6, 4.0, 1.0)
    _icon_chart_card(ax, 7.1, 2.0, 2.6, 2.1, rng)

    # Theme chip
    ax.add_patch(
        FancyBboxPatch(
            (6.0, 5.25),
            3.3,
            0.5,
            boxstyle="round,pad=0.03,rounding_size=0.18",
            facecolor="#dff1ff",
            edgecolor="#9ac4e8",
            linewidth=2,
            zorder=9,
        )
    )
    ax.text(6.15, 5.5, "Exploration mode", fontsize=10, color="#1b3552", zorder=10)

    # Footer
    ax.text(0.7, 0.25, "MIS 6380 • Class 4", fontsize=9.5, color="#58708a", zorder=10)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout(pad=0)
    fig.savefig(out_path, facecolor="white", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a single Class4 slide to PNG")
    parser.add_argument("--slide", type=int, default=1, help="1-based slide number from Class4.md")
    parser.add_argument("--style", choices=["flat", "jetsons"], default="flat")
    parser.add_argument(
        "--out",
        type=str,
        default=None,
        help="Output path. Default: Class4/cartoon_slides/slide_XXX_<style>.png",
    )
    args = parser.parse_args()

    if not MD_FILE.exists():
        raise FileNotFoundError(f"Missing markdown file: {MD_FILE}")

    slides = split_markdown_slides(MD_FILE.read_text(encoding="utf-8"))
    if not (1 <= args.slide <= len(slides)):
        raise ValueError(f"Slide {args.slide} is out of range (1..{len(slides)})")

    slide_text = slides[args.slide - 1]
    title, bullets = extract_title_and_points(slide_text)

    if args.out:
        out_path = Path(args.out)
    else:
        out_path = DEFAULT_OUT_DIR / f"slide_{args.slide:03d}_{args.style}.png"

    if args.style == "jetsons":
        create_jetsons_slide_image(args.slide, title, bullets, slide_text, out_path)
    else:
        create_flat_cartoon_slide_image(args.slide, title, bullets, slide_text, out_path)

    print(f"Created: {out_path}")


if __name__ == "__main__":
    main()
