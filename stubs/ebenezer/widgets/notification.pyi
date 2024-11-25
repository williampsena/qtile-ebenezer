from _typeshed import Incomplete
from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.core.command import build_shell_command as build_shell_command, run_shell_command as run_shell_command
from ebenezer.widgets.helpers.args import build_widget_args as build_widget_args
from libqtile.widget import base

class DunstWidget(base.ThreadPoolText):
    defaults: Incomplete
    count: int
    modal_confirm_cmd: Incomplete
    animated: Incomplete
    bells_index: int
    bells: Incomplete
    foreground_zero: Incomplete
    foreground_count: Incomplete
    def __init__(self, **config) -> None: ...
    foreground: Incomplete
    def poll(self): ...
    def get_bell_icon(self): ...
    def get_notification_count(self): ...
    def show_notifications(self) -> None: ...
    def clear_notifications(self) -> None: ...

def build_notification_widget(settings: AppSettings, kwargs: dict): ...
