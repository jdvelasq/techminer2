"""Color constants (Tableau palettes) exported as ANSI escape sequences.

These use 24-bit ANSI color sequences (\x1b[38;2;R;G;Bm) so they can be
used together with Colorama on terminals that support truecolor. Example:

        from colorama import init, Style
        init()
        from techminer2._internals import colors

        print(colors.TABLEAU10_BLUE + "Hello" + colors.RESET)

This module exposes:
- `RESET`: reset sequence (uses Colorama's reset if available)
- named constants like `TABLEAU10_BLUE`, `TABLEAU10_ORANGE`, ...
- `TABLEAU10_HEX`: list with the original hex strings (in order)
- `TABLEAU10`: list with the ANSI sequences (in order)
"""

from typing import Tuple

try:
    # Try to import Colorama reset for consistency
    from colorama import Style

    RESET = Style.RESET_ALL
except (ImportError, AttributeError):
    RESET = "\x1b[0m"


def _hex_to_rgb(hexcode: str) -> Tuple[int, int, int]:
    hexcode = hexcode.lstrip("#")
    return (
        int(hexcode[0:2], 16),
        int(hexcode[2:4], 16),
        int(hexcode[4:6], 16),
    )


def _rgb_to_ansi(rgb: Tuple[int, int, int]) -> str:
    r, g, b = rgb
    return f"\x1b[38;2;{r};{g};{b}m"


def hex_to_ansi(hexcode: str) -> str:
    """Convert hex color (e.g. '#4E79A7') to ANSI 24-bit foreground sequence."""
    return _rgb_to_ansi(_hex_to_rgb(hexcode))


# Tableau 10 palette (hex) — commonly used Tableau 'Tableau 10' colors
# Source (common reference): community color palettes used across projects
TABLEAU10_HEX = [
    "#4E79A7",
    "#F28E2B",
    "#E15759",
    "#76B7B2",
    "#59A14F",
    "#EDC948",
    "#B07AA1",
    "#FF9DA7",
    "#9C755F",
    "#BAB0AC",
]

# Additional light gray (not part of original Tableau10 but handy)
TABLEAU10_IRON_HEX = "#48494B"
TABLEAU10_IRON = hex_to_ansi(TABLEAU10_IRON_HEX)

TABLEAU10_GLACIER_HEX = "#C5C6C7"
TABLEAU10_GLACIER = hex_to_ansi(TABLEAU10_GLACIER_HEX)

TABLEAU10_TEMPERED_HEX = "#A1AEB1"
TABLEAU10_TEMPERED = hex_to_ansi(TABLEAU10_TEMPERED_HEX)

TABLEAU10_DAVY_HEX = "#595959"
TABLEAU10_DAVY = hex_to_ansi(TABLEAU10_DAVY_HEX)

# Export individual named constants (ANSI sequences)
TABLEAU10_BLUE = hex_to_ansi(TABLEAU10_HEX[0])
TABLEAU10_ORANGE = hex_to_ansi(TABLEAU10_HEX[1])
TABLEAU10_RED = hex_to_ansi(TABLEAU10_HEX[2])
TABLEAU10_TEAL = hex_to_ansi(TABLEAU10_HEX[3])
TABLEAU10_GREEN = hex_to_ansi(TABLEAU10_HEX[4])
TABLEAU10_YELLOW = hex_to_ansi(TABLEAU10_HEX[5])
TABLEAU10_PURPLE = hex_to_ansi(TABLEAU10_HEX[6])
TABLEAU10_PINK = hex_to_ansi(TABLEAU10_HEX[7])
TABLEAU10_BROWN = hex_to_ansi(TABLEAU10_HEX[8])
TABLEAU10_GREY = hex_to_ansi(TABLEAU10_HEX[9])


# Ordered list of ANSI sequences matching `TABLEAU10_HEX`
TABLEAU10 = [
    TABLEAU10_BLUE,
    TABLEAU10_ORANGE,
    TABLEAU10_RED,
    TABLEAU10_TEAL,
    TABLEAU10_GREEN,
    TABLEAU10_YELLOW,
    TABLEAU10_PURPLE,
    TABLEAU10_PINK,
    TABLEAU10_BROWN,
    TABLEAU10_GREY,
]


__all__ = [
    "RESET",
    "TABLEAU10_HEX",
    "TABLEAU10",
    "TABLEAU10_BLUE",
    "TABLEAU10_ORANGE",
    "TABLEAU10_RED",
    "TABLEAU10_TEAL",
    "TABLEAU10_GREEN",
    "TABLEAU10_YELLOW",
    "TABLEAU10_PURPLE",
    "TABLEAU10_PINK",
    "TABLEAU10_BROWN",
    "TABLEAU10_GREY",
    "hex_to_ansi",
]
