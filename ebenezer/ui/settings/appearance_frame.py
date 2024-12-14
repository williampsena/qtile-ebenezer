#!/usr/bin/env python3

import os

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from ebenezer.config.settings import AppSettings
from ebenezer.core.files import resolve_file_path
from ebenezer.core.yaml import update_yaml_property
from ebenezer.ui.settings.helpers import restart_qtile
from ebenezer.ui.settings.styles import build_fonts
from ebenezer.ui.settings.widgets.field import FormField, build_form
from ebenezer.ui.settings.widgets.result_message import ResultMessageWidget

COLORS_CONFIG_FILE = resolve_file_path("$qtile_home/colors.yml")
THEMES_DIR = resolve_file_path("$qtile_home/conf/themes")


class AppearanceFrame(ttk.Frame):
    color_changes: dict[str, str] = {}

    def __init__(self, settings: AppSettings, app: ttk.Frame, parent):
        super().__init__(parent)
        self.app = app
        self.settings = settings
        self.fonts = build_fonts(settings)
        self._build_ui()

    def _load_themes(self):
        themes: list[str] = [""]
        for file in os.listdir(THEMES_DIR):
            if file.endswith(".yaml") or file.endswith(".yml"):
                themes.append(file)
        return themes

    def _update_config(self):
        try:
            colors_updated = self._update_colors_config()

            if not colors_updated:
                self.result_message.set_message(
                    "error", f"✅ No appearance settings to update"
                )
                return

            restart_qtile()
            self.result_message.set_message(
                "success", f"✅ Appearance updated successfully"
            )
        except Exception as e:
            self.result_message.set_message(
                "error", f"❌ Failed to update appearance settings: {e}"
            )

    def _update_colors_config(self) -> bool:
        if not self.color_changes:
            return False

        for key, value in self.color_changes.items():
            update_yaml_property(COLORS_CONFIG_FILE, key, value)

        return True

    def _apply_event(self):
        self._update_config()

    def get_applied_theme(self, settings: AppSettings):
        if settings.colors.theme is None or settings.colors.theme == "":
            return ""

        return os.path.basename(settings.colors.theme)

    def _build_ui(self):
        self.result_message = ResultMessageWidget(
            master=self,
            settings=self.settings,
        )

        self._build_theme_frame()
        self.create_apply_button()

    def create_apply_button(self):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="  Apply",
            command=self._apply_event,
            bootstyle=SUCCESS,
            width=10,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

    def _build_theme_frame(self):
        themes = self._load_themes()

        fields = [
            FormField(
                label="󰉦  Theme",
                value=self.get_applied_theme(self.settings),
                type="list",
                on_value_change=lambda _, v: self.color_changes.update(
                    {"colors.theme": f"{THEMES_DIR}/{v}"}
                ),
                options=themes,
            ),
        ]

        build_form(fields, self.settings, self)
