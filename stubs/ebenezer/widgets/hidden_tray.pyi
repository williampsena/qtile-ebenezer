from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.widgets.backlight import build_backlight_widget as build_backlight_widget
from ebenezer.widgets.helpers.args import build_widget_args as build_widget_args
from ebenezer.widgets.wallpaper import build_wallpaper_widget as build_wallpaper_widget

def build_hidden_tray(settings: AppSettings, kwargs: dict): ...
