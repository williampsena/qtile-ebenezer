from libqtile import widget
from libqtile.config import Key
from libqtile.lazy import lazy

import ebenezer.commands.backlight as backlight_cmd
from ebenezer.config.settings import AppSettings
from ebenezer.core.notify import push_notification_progress
from ebenezer.widgets.helpers.args import build_widget_args

NOTIFICATION_TITLE = "󰃠 Brightness"


def build_backlight_widget(settings: AppSettings, kwargs: dict):
    """
    Build a backlight widget for the Qtile window manager.

    This function creates a backlight widget using the provided settings and additional keyword arguments.
    The widget displays the current backlight level and allows for interaction via mouse callbacks.

    Args:
        settings (AppSettings): An instance of AppSettings containing configuration for fonts, colors, and environment.
        kwargs (dict): Additional keyword arguments to customize the widget.

    Returns:
        widget.Backlight: A configured backlight widget instance.
    """
    default_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "foreground": settings.colors.fg_normal,
        "backlight_name": settings.environment.backlight_name,
        "fmt": " ",
        "padding": 3,
        "mouse_callbacks": {"Button1": _backlight_level()},
    }

    args = build_widget_args(settings, default_args, kwargs)

    return widget.Backlight(**args)


def _get_backlight_level() -> int:
    output = backlight_cmd.backlight_level()

    return int(output.replace("%", "").replace("\n", "") or "0")


def _backlight_up():
    @lazy.function
    def _inner(_):
        level = _get_backlight_level()

        if level >= 100:
            return

        backlight_cmd.backlight_up()
        _push_backlight_notification(NOTIFICATION_TITLE)

    return _inner


def __backlight_down():
    @lazy.function
    def _inner(_):
        backlight_cmd.backlight_down()
        _push_backlight_notification(NOTIFICATION_TITLE)

    return _inner


def _backlight_level():
    @lazy.function
    def _inner(_):
        _push_backlight_notification(NOTIFICATION_TITLE)

    return _inner


def _push_backlight_notification(message: str):
    level = _get_backlight_level()
    message = f"{message} {level}%"
    push_notification_progress(message=message, progress=level)


def setup_backlight_keys():
    """
    Sets up key bindings for adjusting the backlight brightness.

    Args:
        settings (): The application settings object containing configuration.

    Returns:
        list: A list of Key objects for increasing and decreasing the backlight brightness.
    """
    return [
        Key([], "XF86MonBrightnessUp", _backlight_up()),
        Key([], "XF86MonBrightnessDown", __backlight_down()),
    ]
