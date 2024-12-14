from typing import Any

import ttkbootstrap as ttk

from ebenezer.config.settings import AppSettings
from ebenezer.ui.settings.styles import build_fonts


class ResultMessageWidget(ttk.Label):
    def __init__(
        self,
        settings: AppSettings,
        master: Any,
        **kwargs,
    ):
        super().__init__(master, **kwargs)
        self.settings = settings
        self.fonts = build_fonts(settings)
        self._build_ui()

    def reset(self):
        self.configure(text="", foreground=self.settings.colors.fg_normal)
        self.pack_forget()

    def set_message(self, kind: str, message: str):
        if kind == "error":
            self.configure(text=message, foreground=self.settings.colors.fg_red)
        else:
            self.configure(text=message, foreground=self.settings.colors.fg_green)

        self.pack(pady=20)
        self.after(4000, lambda: self.reset())

    def _build_ui(self):
        self.configure(
            text="",
            font=self.fonts.regular,
        )
        self.pack_forget()
