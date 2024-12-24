from libqtile.config import Screen

from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.widgets.bar import build_bar as build_bar

def build_screen(settings: AppSettings) -> Screen: ...
