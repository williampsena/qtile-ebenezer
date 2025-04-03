from typing import Any, Callable

from _typeshed import Incomplete
from libqtile.layout.base import Layout as BaseLayout

from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.config.settings import load_settings_by_files as load_settings_by_files
from ebenezer.widgets.helpers.args import build_widget_args as build_widget_args

CENTER_WINDOWS_TITLES: Incomplete
LAYOUTS: dict[str, Callable[[AppSettings, dict[str, Any]], BaseLayout]]

def build_layouts(settings: AppSettings): ...
def set_floating_window(window) -> None: ...
def centralize_window(settings: AppSettings, window): ...
def is_ebenezer_window(window): ...
