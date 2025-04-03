from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.core.command import lazy_command as lazy_command
from ebenezer.widgets.helpers.args import build_widget_args as build_widget_args

def build_settings_widget(settings: AppSettings, kwargs: dict): ...
