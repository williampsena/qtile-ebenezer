import requests
from libqtile import widget
from libqtile.lazy import lazy
from libqtile.log_utils import logger
from libqtile.widget import base

from ebenezer.config.settings import AppSettings
from ebenezer.core.command import build_shell_command
from ebenezer.core.requests import request_retry
from ebenezer.widgets.helpers.args import build_widget_args


class GitHubNotifications(base.ThreadPoolText):
    """
    A widget that fetches GitHub notifications.

    Attributes:
        orientations (str): The orientation of the widget, set to horizontal.
        defaults (list): Default configuration options for the widget.

    Args:
        **config: Arbitrary keyword arguments for widget configuration.

    Methods:
        __init__(**config):
            Initializes the GitHubNotifications widget with the given configuration.

        poll():
            Fetches the latest GitHub notifications and updates the widget display.
            Returns a string representing the number of notifications or an error message.
    """

    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ("update_interval", 10, "Update interval in seconds"),
        ("token", None, "GitHub Personal Access Token"),
    ]

    def __init__(self, **config):
        super().__init__("", **config)

        self.settings = config.pop("settings")
        self.icon = config.pop("icon_widget")
        self.icon.base_text = self.icon.text or ""
        self.token = config.get(
            "token", self.settings.environment.github_notifications_token
        )
        self.add_defaults(GitHubNotifications.defaults)

    def poll(self):
        if self.token is None:
            return "No github token"

        try:

            def _do_request():
                headers = {
                    "Authorization": f"token {self.token}",
                    "Accept": "application/vnd.github.v3+json",
                }

                return requests.get(
                    "https://api.github.com/notifications", headers=headers
                )

            response = request_retry(_do_request)
            status_code = response.status_code

            if status_code == 200:
                notifications = response.json()
                count = len(notifications)

                if count == 0:
                    self.icon.foreground = self.icon.foreground_normal
                    self.icon.text = ""
                    return ""
                else:
                    self.icon.text = self.icon.base_text
                    self.icon.foreground = self.icon.foreground_alert
                    return f"{count}+"
            else:
                logger.warning("GitHub API Error... {status_code}")
                return " "
        except Exception as e:
            logger.warning(f"GitHub Notifications Error: {e}", exc_info=True)
            return " "


def build_github_widget(settings: AppSettings, kwargs: dict):
    """
    Build a GitHub widget for the Qtile window manager.

    This function constructs a GitHub widget using the provided settings and keyword arguments.
    It creates an icon widget and a GitHub notifications widget with the specified configurations.

    Args:
        settings (AppSettings): The application settings containing fonts, colors, and other configurations.
        kwargs (dict): Additional keyword arguments for customizing the widget. It can contain:
            - "icon" (dict): Custom arguments for the icon widget.
            - "widget" (dict): Custom arguments for the GitHub notifications widget.

    Returns:
        list: A list containing the icon widget and the GitHub notifications widget.
    """
    icon_widget = _build_github_icon_widget(settings, kwargs.get("icon", {}))

    default_args = {
        "icon_widget": icon_widget,
        "settings": settings,
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "padding": 4,
        "foreground": settings.colors.fg_normal,
        "background": settings.colors.bg_topbar_arrow,
    }

    args = build_widget_args(settings, default_args, kwargs.get("widget", {}))

    return [
        icon_widget,
        GitHubNotifications(**args),
    ]


def _build_github_icon_widget(settings: AppSettings, kwargs: dict):
    default_icon_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "padding": 6,
        "foreground": settings.colors.fg_white,
        "foreground_normal": settings.colors.fg_white,
        "foreground_alert": settings.colors.fg_yellow,
        "background": settings.colors.bg_topbar_arrow,
        "mouse_callbacks": {"Button1": _go_to_notifications_url(settings)},
    }

    icon_args = build_widget_args(settings, default_icon_args, kwargs)

    return widget.TextBox(f"{icon_args.pop("text", "")}", **icon_args)


def _go_to_notifications_url(settings: AppSettings):
    cmd = settings.commands.get("open_url")

    if cmd is None:
        return

    return lazy.spawn(build_shell_command(cmd, url="https://github.com/notifications"))
