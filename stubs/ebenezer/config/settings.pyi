from typing import Any

from _typeshed import Incomplete

from ebenezer.config.applications import (
    AppSettingsApplications as AppSettingsApplications,
)
from ebenezer.config.bar import AppSettingsBar as AppSettingsBar
from ebenezer.config.colors import AppSettingsColors as AppSettingsColors
from ebenezer.config.environment import AppSettingsEnvironment as AppSettingsEnvironment
from ebenezer.config.fonts import AppSettingsFonts as AppSettingsFonts
from ebenezer.config.keybindings import AppSettingsKeyBinding as AppSettingsKeyBinding
from ebenezer.config.keybindings import build_keybindings as build_keybindings
from ebenezer.config.loader import load_raw_settings as load_raw_settings
from ebenezer.config.lock_screen import AppSettingsLockScreen as AppSettingsLockScreen
from ebenezer.config.monitoring import AppSettingsMonitoring as AppSettingsMonitoring
from ebenezer.core.files import qtile_home as qtile_home

class AppSettings:
    applications: AppSettingsApplications
    bar: AppSettingsBar
    colors: AppSettingsColors
    commands: dict[str, str]
    environment: Incomplete
    floating: dict[str, list[str]]
    fonts: Incomplete
    groups: list[Any]
    groups_layout: dict[str, str]
    layouts: dict[str, dict]
    keybindings: list[AppSettingsKeyBinding]
    lock_screen: Incomplete
    monitoring: AppSettingsMonitoring
    startup: dict[str, str]
    def __init__(self, **kwargs) -> None: ...

def load_settings_by_files(
    config_filepath: Incomplete | None = None,
    colors_filepath: Incomplete | None = None,
    applications_filepath: Incomplete | None = None,
) -> AppSettings: ...
def load_settings(raw_settings: dict) -> AppSettings: ...
