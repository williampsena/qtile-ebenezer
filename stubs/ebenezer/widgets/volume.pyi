from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.core.notify import push_notification as push_notification
from ebenezer.core.notify import (
    push_notification_progress as push_notification_progress,
)
from ebenezer.widgets.helpers.args import build_widget_args as build_widget_args

def build_volume_widget(settings: AppSettings, kwargs: dict): ...
def setup_volume_keys(settings: AppSettings): ...
