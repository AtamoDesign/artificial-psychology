"""Minimal color-shape visual code, sized to human working memory.

Six symbols, each a fixed color + shape pair, on a neutral background.
Colors are the Okabe-Ito colorblind-safe palette; shape is a redundant
channel so the code survives color-vision deficiency and imperfect vision
models. See docs/visual-code-spec.md.
"""
from __future__ import annotations

from dataclasses import dataclass

SPEC_VERSION = "0.1"

# Working-memory limits (Cowan 2001: ~4 chunks; Miller 1956: 7 +/- 2).
MAX_VOCABULARY = 7
MAX_MESSAGE_LENGTH = 4

BACKGROUND_LIGHT = "#F2F2F2"
BACKGROUND_DARK = "#2B2B2B"


@dataclass(frozen=True)
class Symbol:
    name: str
    hex: str
    shape: str

    @property
    def rgb(self) -> tuple[int, int, int]:
        h = self.hex.lstrip("#")
        return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


SYMBOLS: tuple[Symbol, ...] = (
    Symbol("blue", "#0072B2", "circle"),
    Symbol("orange", "#E69F00", "square"),
    Symbol("green", "#009E73", "triangle"),
    Symbol("yellow", "#F0E442", "diamond"),
    Symbol("red", "#D55E00", "cross"),
    Symbol("pink", "#CC79A7", "star"),
)

BY_NAME = {s.name: s for s in SYMBOLS}


def parse_message(text: str) -> list[Symbol]:
    """Parse a message like "blue green red" into symbols.

    Raises ValueError for unknown names or messages longer than
    MAX_MESSAGE_LENGTH.
    """
    names = text.lower().replace(",", " ").replace("-", " ").split()
    unknown = [n for n in names if n not in BY_NAME]
    if unknown:
        raise ValueError(f"unknown symbol(s): {', '.join(unknown)}")
    if len(names) > MAX_MESSAGE_LENGTH:
        raise ValueError(
            f"message has {len(names)} symbols; limit is {MAX_MESSAGE_LENGTH}"
        )
    return [BY_NAME[n] for n in names]


def format_message(symbols: list[Symbol]) -> str:
    return " ".join(s.name for s in symbols)
