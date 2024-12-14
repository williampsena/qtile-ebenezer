from tkinter import ttk

from ebenezer.config.settings import AppSettings
from ebenezer.ui.settings.styles import build_fonts


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
