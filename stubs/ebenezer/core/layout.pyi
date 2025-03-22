from ebenezer.config.settings import AppSettings as AppSettings
from libqtile.layout.base import Layout as BaseLayout
from typing import Any, Callable

LAYOUTS: dict[str, Callable[[AppSettings, dict[str, Any]], BaseLayout]]

def build_layouts(settings: AppSettings): ...
