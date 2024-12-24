from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.widgets.bar import build_bar as build_bar
from libqtile.config import Screen

def build_screen(settings: AppSettings) -> Screen: ...
