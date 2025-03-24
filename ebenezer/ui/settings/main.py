import signal
import sys

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from ebenezer.config.settings import load_settings_by_files
from ebenezer.core.theme import apply_theme_color
from ebenezer.ui.settings.about_frame import AboutFrame
from ebenezer.ui.settings.appearance_frame import AppearanceFrame
from ebenezer.ui.settings.environment_frame import EnvironmentFrame
from ebenezer.ui.settings.styles import build_fonts, build_style
from ebenezer.ui.settings.wallpaper_frame import WallpaperFrame

THEME_NAME = "darkly"


class EbenezerManager(ttk.Frame):
    def __init__(self, master, theme_name: str):
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)

        self.theme_name = theme_name
        self.load_settings()
        self.fonts = build_fonts(self.settings)
        self.styles = build_style(self.settings, self.theme_name, self)

        self.build_ui()

    def load_settings(self):
        self.settings = load_settings_by_files()
        self.settings = apply_theme_color(self.settings)

    def _close_window(self):
        self.master.destroy()
        sys.exit(0)

    def _handle_change_tab(
        self, tab_name: str, buttons: dict[str, ttk.Button]
    ) -> callable:
        def _inner(_):
            for button in buttons.values():
                button.config(style="Tab.TLabel")

            buttons.get(tab_name).config(style="TabSelected.TLabel")
            self._show_tab(tab_name)

        return _inner

    def _sidebar(self):
        tabs = {
            "about": {"label": " ", "build": self._build_about_tab},
            "appearance": {
                "label": " ",
                "build": self._build_appearance_tab,
            },
            "wallpaper": {
                "label": "󰸉 ",
                "build": self._build_wallpaper_tab,
            },
            "environment": {
                "label": "󰘦 ",
                "build": self._build_environment_tab,
            },
            "quit": {"label": "󰅙 "},
        }

        self.sidebar_frame = ttk.Frame(self, width=10, style="Sidebar.TFrame")
        self.sidebar_frame.pack(side="left", fill="y")

        self.tab_frames: dict[str, ttk.Frame] = {}

        buttons: dict[str, ttk.Button] = {}

        for tab_name in tabs:
            tab = tabs.get(tab_name)
            tab_label = tab.get("label")
            tab_build = tab.get("build")

            button = ttk.Label(
                self.sidebar_frame,
                text=tab_label,
                anchor="w",
                cursor="hand2",
                style="Tab.TLabel",
            )
            buttons[tab_name] = button
            button.pack(side="top", fill="x", expand=False, padx=(10, 20), pady=10)

            if callable(tab_build):
                tab_frame = tab_build(self)
            else:
                tab_frame = ttk.Frame(self)

            self.tab_frames[tab_name] = tab_frame

        for tab_name in buttons:
            button = buttons.get(tab_name)
            button.bind(
                "<Button-1>", self._handle_change_tab(tab_name, buttons=buttons)
            )

        self._handle_change_tab("about", buttons=buttons)(None)

    def _build_appearance_tab(self, parent: ttk.Frame):
        return AppearanceFrame(
            app=self,
            settings=self.settings,
            parent=parent,
        )

    def _build_wallpaper_tab(self, parent: ttk.Frame):
        return WallpaperFrame(
            app=self,
            settings=self.settings,
            parent=parent,
        )

    def _build_environment_tab(self, parent: ttk.Frame):
        return EnvironmentFrame(
            app=self,
            settings=self.settings,
            parent=parent,
        )

    def _build_about_tab(self, parent: ttk.Frame):
        return AboutFrame(
            app=self,
            settings=self.settings,
            parent=parent,
        )

    def _show_tab(self, tab: str):
        if tab == "quit":
            return self._close_window()

        for tab_name, tab_frame in self.tab_frames.items():
            tab_frame.pack_forget()

            if tab_name == tab:
                tab_frame.pack(side="top", fill="x", expand=False, padx=10, pady=10)
                tab_frame.tkraise()

    def build_ui(self):
        self._sidebar()


def handle_sigint(signal_received, frame):
    print("\nExiting application...")
    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, handle_sigint)

    app = ttk.Window("ebenezer - configuration manager", themename=THEME_NAME)
    app.update_idletasks()

    app.wm_minsize(1000, 600)
    app.geometry("1000x600")

    EbenezerManager(app, theme_name=THEME_NAME)
    app.mainloop()
