from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.core.notify import push_notification_progress as push_notification_progress
from ebenezer.widgets.helpers.args import build_widget_args as build_widget_args

NOTIFICATION_TITLE: str

def build_backlight_widget(settings: AppSettings, kwargs: dict): ...
def setup_backlight_keys(): ...
