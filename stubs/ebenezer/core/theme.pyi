from _typeshed import Incomplete
from ebenezer.config.settings import AppSettings as AppSettings, AppSettingsColors as AppSettingsColors
from ebenezer.core.dict import merge_dicts_recursive as merge_dicts_recursive
from ebenezer.core.files import resolve_file_path as resolve_file_path
from ebenezer.core.yaml import read_yaml_file as read_yaml_file

ROFI_TEMPLATES: Incomplete
DUNSTRC_HOME_PATH: str

def maybe_preload_colors(settings: AppSettings) -> AppSettings: ...
def preload_colors(settings: AppSettings, complete: bool = False) -> AppSettings: ...
def apply_theme_color(settings: AppSettings) -> AppSettings: ...
