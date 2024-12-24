#!/usr/bin/env python3


import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from ebenezer.config.settings import AppSettings
from ebenezer.core.files import resolve_file_path
from ebenezer.core.yaml import update_yaml_property
from ebenezer.ui.settings.helpers import restart_qtile
from ebenezer.ui.settings.styles import build_fonts
from ebenezer.ui.settings.widgets.field import FormField, build_form
from ebenezer.ui.settings.widgets.result_message import ResultMessageWidget

SETTINGS_CONFIG_FILE = resolve_file_path("$qtile_home/config.yml")


class EnvironmentFrame(ttk.Frame):
    color_changes: dict[str, str] = {}
    settings_changes: dict[str, str] = {}

    def __init__(self, settings: AppSettings, app: ttk.Frame, parent):
        super().__init__(parent)
        self.app = app
        self.settings = settings
        self.fonts = build_fonts(settings)
        self._build_ui()

    def _update_config(self):
        try:
            settings_updated = self._update_settings_config()

            if not settings_updated:
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

    def _update_settings_config(self) -> bool:
        if not self.settings_changes:
            return False

        for key, value in self.settings_changes.items():
            update_yaml_property(SETTINGS_CONFIG_FILE, key, value)

        return True

    def _build_ui(self):
        self.result_message = ResultMessageWidget(
            master=self,
            settings=self.settings,
        )

        self._build_component()
        self.create_apply_button()

    def _apply_event(self):
        self._update_config()

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

    def _build_form_field_text(self, label: str, key: str, value: str) -> FormField:
        return FormField(
            label=label,
            value=value,
            type="text",
            on_value_change=lambda _, v: self.settings_changes.update(
                {f"environment.{key}": v}
            ),
        )

    def _build_component(self):
        env = self.settings.environment

        fields = [
            self._build_form_field_text("   Mod Key", "modkey", env.modkey),
            self._build_form_field_text("   Terminal", "terminal", env.terminal),
            self._build_form_field_text("   Browser", "browser", env.browser),
            self._build_form_field_text("󰌽  OS Logo Path", "os_logo", env.os_logo),
            self._build_form_field_text(
                "  OS Logo Icon", "os_logo_icon", env.os_logo_icon
            ),
            self._build_form_field_text(
                "  OS Logo Icon Color", "os_logo_icon_color", env.os_logo_icon_color
            ),
            self._build_form_field_text(
                "󰍹   Backlight Name", "backlight_name", env.backlight_name
            ),
            self._build_form_field_text(
                "󰖐  Weather API Key", "weather_api_key", env.weather_api_key
            ),
            self._build_form_field_text(
                "   Weather City ID", "weather_city_id", env.city_id
            ),
            self._build_form_field_text(
                "   Github Notifications Token",
                "github_notifications_token",
                env.github_notifications_token,
            ),
            self._build_form_field_text("  Scripts Path", "scripts", env.scripts),
        ]

        build_form(fields, self.settings, self, label_width=30)
