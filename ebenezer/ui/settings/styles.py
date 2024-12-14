from ebenezer.config.settings import AppSettings
from typing import NamedTuple


class FontStyle(NamedTuple):
    family: str
    size: int
    style: str = ""


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


def build_fonts(settings: AppSettings):
    return FontStyles(
        small=FontStyle(family=settings.fonts.font, size=14),
        regular=FontStyle(family=settings.fonts.font, size=16),
        medium=FontStyle(family=settings.fonts.font, size=20),
        big=FontStyle(family=settings.fonts.font, size=30),
        italic_small=FontStyle(family=settings.fonts.font, size=14, style="italic"),
        italic_regular=FontStyle(family=settings.fonts.font, size=16, style="italic"),
        italic_medium=FontStyle(family=settings.fonts.font, size=20, style="italic"),
        italic_big=FontStyle(family=settings.fonts.font, size=30, style="italic"),
        bold_small=FontStyle(family=settings.fonts.font, size=14, style="bold"),
        bold_regular=FontStyle(family=settings.fonts.font, size=16, style="bold"),
        bold_medium=FontStyle(family=settings.fonts.font, size=20, style="bold"),
        bold_big=FontStyle(family=settings.fonts.font, size=30, style="bold"),
    )
