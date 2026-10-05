"""Render the symbol sheet on light and dark backgrounds."""
from pathlib import Path

from artpsych.render import render_sheet
from artpsych.visual_code import BACKGROUND_DARK, BACKGROUND_LIGHT

out = Path(__file__).resolve().parents[1] / "docs"
render_sheet(background=BACKGROUND_LIGHT).save(out / "symbols-light.png")
render_sheet(background=BACKGROUND_DARK).save(out / "symbols-dark.png")
print(f"wrote {out / 'symbols-light.png'} and {out / 'symbols-dark.png'}")
