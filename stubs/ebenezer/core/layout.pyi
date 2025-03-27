from typing import Any, Callable

from libqtile.layout.base import Layout as BaseLayout

from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.config.settings import load_settings_by_files as load_settings_by_files

LAYOUTS: dict[str, Callable[[AppSettings, dict[str, Any]], BaseLayout]]

def build_layouts(settings: AppSettings): ...
def set_floating_window(window) -> None: ...
