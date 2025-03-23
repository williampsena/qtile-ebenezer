from tkinter import ttk
from typing import NamedTuple

from ebenezer.config.settings import AppSettings as AppSettings

class FontStyle(NamedTuple):
    family: str
    size: int
    style: str = ...

class FontStyles(NamedTuple):
    small: FontStyle
    regular: FontStyle
    medium: FontStyle
    big: FontStyle
    italic_small: FontStyle
    italic_regular: FontStyle
    italic_medium: FontStyle
    italic_big: FontStyle
    bold_small: FontStyle
    bold_regular: FontStyle
    bold_medium: FontStyle
    bold_big: FontStyle

def build_fonts(settings: AppSettings): ...
def build_style(
    settings: AppSettings, theme_name: str, root: ttk.Frame
) -> ttk.Style: ...
