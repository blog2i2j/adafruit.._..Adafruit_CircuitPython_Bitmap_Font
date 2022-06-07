# SPDX-FileCopyrightText: 2019 Scott Shawcroft for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_bitmap_font.bitmap_font`
====================================================

Loads bitmap glyphs from a variety of font.

* Author(s): Scott Shawcroft

Implementation Notes
--------------------

**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

try:
    from typing import Optional, Union
except ImportError:
    pass

from displayio import Bitmap
from . import bdf
from . import pcf
from . import ttf

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Bitmap_Font.git"


def load_font(
    filename: str, bitmap: Optional[Bitmap] = None
) -> Union[bdf.BDF, pcf.PCF, ttf.TTF, None]:
    """Loads a font file. Returns None if unsupported."""
    # pylint: disable=import-outside-toplevel, consider-using-with
    if not bitmap:
        bitmap = Bitmap
    font_file = open(filename, "rb")
    first_four = font_file.read(4)
    if filename.endswith("bdf") and first_four == b"STAR":
        return bdf.BDF(font_file, bitmap)
    if filename.endswith("pcf") and first_four == b"\x01fcp":
        return pcf.PCF(font_file, bitmap)
    if filename.endswith("ttf") and first_four == b"\x00\x01\x00\x00":
        return ttf.TTF(font_file, bitmap)

    raise ValueError("Unknown magic number %r" % first_four)
