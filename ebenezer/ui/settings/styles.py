from tkinter import ttk
from typing import NamedTuple

from ebenezer.config.settings import AppSettings


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


def build_style(settings: AppSettings, theme_name: str, root: ttk.Frame) -> ttk.Style:
    fonts = build_fonts(settings)
    style = ttk.Style()
    style.theme_use(theme_name)

    style.configure("TEntry", font=fonts.big)

    style.configure(
        "Form.TEntry",
        font=fonts.medium,
        padding=5,
    )

    style.configure(
        "Form.TCombobox",
        font=fonts.medium,
        padding=5,
    )

    style.map("Form.TCombobox", font=[("readonly", fonts.medium)])

    style.configure(
        "Sidebar.TFrame",
        foreground=settings.colors.fg_white,
    )

    style.configure(
        "Tab.TLabel",
        foreground=settings.colors.fg_gray,
        font=fonts.regular,
        padding=10,
    )
    style.configure(
        "TabSelected.TLabel",
        font=fonts.medium,
        foreground=settings.colors.fg_white,
        padding=10,
    )

    style.configure(".", font=fonts.regular)

    root.option_add("*TCombobox*Listbox.font", fonts.regular)

    return style
