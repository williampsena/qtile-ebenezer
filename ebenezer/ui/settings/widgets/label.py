import webbrowser

import ttkbootstrap as ttk

from ebenezer.config.settings import AppSettings
from ebenezer.ui.settings.styles import FontStyles


def _open_url(url):
    webbrowser.open_new(url)


def build_label(
    parent_frame: ttk.Frame,
    app: ttk.Window,
    settings: AppSettings,
    text: str,
    font: FontStyles = None,
    link: str = None,
    cursor: str = None,
    text_color: str = None,
    bootstyle: str = None,
    justify: str = None,
) -> ttk.Label:
    label = ttk.Label(
        master=parent_frame,
        text=text,
        font=font,
        foreground=text_color or settings.colors.fg_normal,
        justify=justify,
        bootstyle=bootstyle,
        wraplength=int(app.winfo_width() * 0.8),
        cursor=cursor,
    )

    if link:
        label.bind("<Button-1>", lambda e: _open_url(link))

    return label
