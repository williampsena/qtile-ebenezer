from _typeshed import Incomplete

from ebenezer.config.keybindings import AppSettingsKeyBinding as AppSettingsKeyBinding
from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.core.command import lazy_spawn as lazy_spawn
from ebenezer.widgets.backlight import setup_backlight_keys as setup_backlight_keys
from ebenezer.widgets.volume import setup_volume_keys as setup_volume_keys

ACTIONS: Incomplete

def build_keys(settings: AppSettings): ...
