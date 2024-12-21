import importlib.metadata
import webbrowser

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from ebenezer.config.settings import AppSettings
from ebenezer.ui.settings.styles import build_fonts
from ebenezer.ui.settings.widgets.label import build_label


class AboutFrame(ttk.Frame):
    settings: AppSettings

    DESCRIPTION = (
        "This project offers a range of widgets and behaviors, from Desktop to Qtile Tiling Window Manager. "
        '\n\nThis theme was named Ebenezer 🪨, which means "stone of helper.".'
    )

    QUOTE = 'The quote is from I Samuel 7. After defeating the Philistines, Samuel raises his Ebenezer, declaring that God defeated the enemies on this spot. As a result, "hither by thy help I come." So I hope this stone helps you in your environment and, more importantly, in your life. 🙏🏿'

    def __init__(self, settings: AppSettings, app: ttk.Window, parent):
        super().__init__(parent)
        self.app = app
        self.settings = settings
        self.fonts = build_fonts(settings)
        self._build_ui()

    def _open_url(self, url):
        webbrowser.open_new(url)

    def _version(self):
        try:
            return importlib.metadata.version("qtile-ebenezer")
        except:
            return "dev"

    def _build_ui(self):
        title = build_label(
            parent_frame=self,
            app=self.app,
            settings=self.settings,
            font=self.fonts.bold_medium,
            text="Qtile Ebenezer",
            text_color=self.settings.colors.fg_selected,
        )
        title.pack(fill=X, expand=YES, pady=(15, 10))

        description = build_label(
            parent_frame=self,
            app=self.app,
            settings=self.settings,
            font=self.fonts.italic_medium,
            text=self.DESCRIPTION,
            justify="left",
        )

        description.configure(wraplength=600)
        description.pack(fill=X, expand=YES, pady=(15, 10))

        quote = build_label(
            parent_frame=self,
            app=self.app,
            settings=self.settings,
            text=self.QUOTE,
            justify="left",
            font=self.fonts.italic_medium,
        )

        quote.configure(wraplength=600)
        quote.pack(fill=X, expand=YES, pady=(15, 10))

        link = build_label(
            parent_frame=self,
            app=self.app,
            settings=self.settings,
            text=f"qtile-ebenezer@{self._version()}",
            text_color=self.settings.colors.fg_selected,
            link=("https://github.com/williampsena/qtile-ebenezer"),
            cursor="hand2",
        )

        link.pack(fill=X, expand=YES, pady=(15, 10))

        author = build_label(
            parent_frame=self,
            app=self.app,
            settings=self.settings,
            text="@williampsena",
            text_color=self.settings.colors.fg_selected,
            link=("https://github.com/williampsena"),
            cursor="hand2",
        )

        author.pack(fill=X, expand=YES, pady=(15, 10))
