from libqtile import widget
from libqtile.config import Key
from libqtile.lazy import lazy

from ebenezer.config.settings import AppSettings
from ebenezer.core.command import run_shell_command, run_shell_command_stdout
from ebenezer.core.notify import push_notification_progress
from ebenezer.widgets.helpers.args import build_widget_args


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
        "mouse_callbacks": {"Button1": _backlight_level(settings)},
    }

    args = build_widget_args(settings, default_args, kwargs)

    return widget.Backlight(**args)


def _get_backlight_level(settings: AppSettings):
    cmd = settings.commands.get("backlight_level")

    if cmd is None:
        return "0"

    output = run_shell_command_stdout(cmd)

    return output.stdout.replace("%", "").replace("\n", "")


def _backlight_up(settings: AppSettings):
    cmd = settings.commands.get("backlight_up")

    @lazy.function
    def inner(qtile):
        level = int(_get_backlight_level(settings) or "0")

        if level >= 100:
            return

        if cmd:
            run_shell_command(cmd)

        __push_backlight_notification(settings, "󰃠 Brightness")

    return inner


def __backlight_down(settings: AppSettings):
    cmd = settings.commands.get("backlight_down")

    @lazy.function
    def inner(qtile):
        if cmd:
            run_shell_command(cmd)

        __push_backlight_notification(settings, "󰃠 Brightness")

    return inner


def _backlight_level(settings: AppSettings):
    @lazy.function
    def inner(qtile):
        __push_backlight_notification(settings, "󰃠 Brightness")

    return inner


def __push_backlight_notification(settings: AppSettings, message: str):
    level = _get_backlight_level(settings) or "0"
    message = f"{message} {level}%"
    push_notification_progress(message=message, progress=int(level))


def setup_backlight_keys(settings: AppSettings):
    """
    Sets up key bindings for adjusting the backlight brightness.

    Args:
        settings (AppSettings): The application settings object containing configuration.

    Returns:
        list: A list of Key objects for increasing and decreasing the backlight brightness.
    """
    return [
        Key([], "XF86MonBrightnessUp", _backlight_up(settings)),
        Key([], "XF86MonBrightnessDown", __backlight_down(settings)),
    ]
