"""Render symbols to images with Pillow (optional dependency)."""
from __future__ import annotations

import math

from .visual_code import BACKGROUND_LIGHT, SYMBOLS, Symbol


def _shape_points(shape: str, cx: float, cy: float, r: float) -> list[tuple[float, float]]:
    if shape == "square":
        return [(cx - r, cy - r), (cx + r, cy - r), (cx + r, cy + r), (cx - r, cy + r)]
    if shape == "triangle":
        return [(cx, cy - r), (cx + r, cy + r * 0.8), (cx - r, cy + r * 0.8)]
    if shape == "diamond":
        return [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
    if shape == "cross":
        w = r * 0.38
        return [
            (cx - w, cy - r), (cx + w, cy - r), (cx + w, cy - w), (cx + r, cy - w),
            (cx + r, cy + w), (cx + w, cy + w), (cx + w, cy + r), (cx - w, cy + r),
            (cx - w, cy + w), (cx - r, cy + w), (cx - r, cy - w), (cx - w, cy - w),
        ]
    if shape == "star":
        pts = []
        for i in range(10):
            rad = r if i % 2 == 0 else r * 0.45
            a = -math.pi / 2 + i * math.pi / 5
            pts.append((cx + rad * math.cos(a), cy + rad * math.sin(a)))
        return pts
    raise ValueError(f"unknown shape: {shape}")


def render_symbol(symbol: Symbol, size: int = 128, background: str = BACKGROUND_LIGHT):
    from PIL import Image, ImageDraw

    img = Image.new("RGB", (size, size), background)
    draw = ImageDraw.Draw(img)
    c, r = size / 2, size * 0.36
    if symbol.shape == "circle":
        draw.ellipse([c - r, c - r, c + r, c + r], fill=symbol.hex)
    else:
        draw.polygon(_shape_points(symbol.shape, c, c, r), fill=symbol.hex)
    return img


def render_sheet(symbols=SYMBOLS, size: int = 128, background: str = BACKGROUND_LIGHT):
    """All symbols in one row, for READMEs and stimulus checks."""
    from PIL import Image

    sheet = Image.new("RGB", (size * len(symbols), size), background)
    for i, s in enumerate(symbols):
        sheet.paste(render_symbol(s, size, background), (i * size, 0))
    return sheet
