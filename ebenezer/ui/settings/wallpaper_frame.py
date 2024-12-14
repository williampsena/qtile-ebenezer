import os

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from ebenezer.commands.helpers import run_command
from ebenezer.config.settings import AppSettings
from ebenezer.core.files import resolve_file_path
from ebenezer.core.yaml import update_yaml_property
from ebenezer.ui.settings.helpers import restart_qtile
from ebenezer.ui.settings.styles import build_fonts
from ebenezer.ui.settings.widgets.field import FormField, build_form
from ebenezer.ui.settings.widgets.result_message import ResultMessageWidget

SETTINGS_CONFIG_FILE = resolve_file_path("$qtile_home/config.yml")
THEMES_DIR = resolve_file_path("$qtile_home/conf/themes")


class WallpaperFrame(ttk.Frame):
    settings_changes: dict[str, str] = {}

    def __init__(self, settings: AppSettings, app: ttk.Frame, parent):
        super().__init__(parent)
        self.app = app
        self.settings = settings
        self.fonts = build_fonts(settings)
        self.path = ttk.StringVar(value=settings.environment.wallpaper_dir)
        self.timeout = ttk.StringVar(value=str(settings.environment.wallpaper_timeout))

        self._build_component()

    def _build_component(self):
        self.result_message = ResultMessageWidget(
            master=self,
            settings=self.settings,
        )

        fields = [
            FormField(
                label="  Path",
                value=self.settings.environment.wallpaper_dir,
                type="text",
                on_value_change=lambda _, v: self.settings_changes.update(
                    {"environment.wallpaper_dir": v}
                ),
            ),
            FormField(
                label="  Timeout",
                value=self.settings.environment.wallpaper_timeout,
                type="number",
                on_value_change=lambda _, v: self.settings_changes.update(
                    {"environment.wallpaper_timeout": int(v or "0")}
                ),
            ),
        ]

        build_form(fields, self.settings, self)
        self.create_apply_button()

    def create_apply_button(self):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="  Apply",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=10,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

    def _reload_wallpaper(self):
        wallpaper_dir = self.settings_changes["environment.wallpaper_dir"]

        if not wallpaper_dir:
            return

        run_command(f"ebenezer wallpaper set {wallpaper_dir}")

    def _load_themes(self):
        themes = [""]
        for file in os.listdir(THEMES_DIR):
            if file.endswith(".yaml") or file.endswith(".yml"):
                themes.append(file)
        return themes

    def _update_config(self):
        try:
            settings_updated = self._update_settings_config()

            if not settings_updated:
                self.result_message.set_message(
                    "error", f"✅ No appearance settings to update"
                )
                return

            restart_qtile()
            self._reload_wallpaper()
            self.result_message.set_message(
                "success", f"✅ Appearance updated successfully"
            )
        except Exception as e:
            self.result_message.set_message(
                "error", f"❌ Failed to update appearance settings: {e}"
            )

    def _update_settings_config(self) -> bool:
        if not self.settings_changes:
            return False

        for key, value in self.settings_changes.items():
            update_yaml_property(SETTINGS_CONFIG_FILE, key, value)

        return True

    def _apply_theme_event(self):
        self._update_config()

    def on_submit(self):
        self._apply_theme_event()
        return self.path.get(), self.timeout.get()
