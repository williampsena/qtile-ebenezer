from typing import Any, Callable

from libqtile.layout.base import Layout as BaseLayout

from ebenezer.config.settings import AppSettings as AppSettings

LAYOUTS: dict[str, Callable[[AppSettings, dict[str, Any]], BaseLayout]]

def build_layouts(settings: AppSettings): ...
