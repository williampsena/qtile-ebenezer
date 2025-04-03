from typing import NamedTuple

from _typeshed import Incomplete

from ebenezer.config.keybindings import AppSettingsKeyBinding as AppSettingsKeyBinding
from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.config.settings import load_settings_by_files as load_settings_by_files
from ebenezer.core.command import lazy_spawn as lazy_spawn
from ebenezer.widgets.backlight import setup_backlight_keys as setup_backlight_keys
from ebenezer.widgets.volume import setup_volume_keys as setup_volume_keys

class ColorKeybindingGroup(NamedTuple):
    name: str
    foreground_ansi: str = ...
    background_ansi: str = ...
    foreground: str = ...
    background: str = ...

COLOR_KEYBINDING_GROUPS: Incomplete
ACTIONS: Incomplete

def build_keys(settings: AppSettings): ...
def fetch_keybindings_text(settings: AppSettings | None = None) -> str: ...
