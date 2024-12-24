from _typeshed import Incomplete
from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.core.command import build_shell_command as build_shell_command
from ebenezer.core.requests import request_retry as request_retry
from ebenezer.widgets.helpers.args import build_widget_args as build_widget_args
from libqtile.widget import base

class GitHubNotifications(base.ThreadPoolText):
    orientations: Incomplete
    defaults: Incomplete
    settings: Incomplete
    icon: Incomplete
    token: Incomplete
    def __init__(self, **config) -> None: ...
    def poll(self): ...

def build_github_widget(settings: AppSettings, kwargs: dict): ...
