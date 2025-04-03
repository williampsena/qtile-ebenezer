import ttkbootstrap as ttk
from _typeshed import Incomplete
from ttkbootstrap.constants import *

from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.core.files import resolve_file_path as resolve_file_path
from ebenezer.core.yaml import update_yaml_property as update_yaml_property
from ebenezer.ui.settings.helpers import restart_qtile as restart_qtile
from ebenezer.ui.settings.styles import build_fonts as build_fonts
from ebenezer.ui.settings.widgets.field import FormField as FormField
from ebenezer.ui.settings.widgets.field import build_form as build_form
from ebenezer.ui.settings.widgets.result_message import (
    ResultMessageWidget as ResultMessageWidget,
)

COLORS_CONFIG_FILE: Incomplete
THEMES_DIR: Incomplete

class AppearanceFrame(ttk.Frame):
    color_changes: dict[str, str]
    app: Incomplete
    settings: Incomplete
    fonts: Incomplete
    def __init__(self, settings: AppSettings, app: ttk.Frame, parent) -> None: ...
    def get_applied_theme(self, settings: AppSettings): ...
    def create_apply_button(self) -> None: ...
