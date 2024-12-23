from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.core.command import run_shell_command
from ebenezer.widgets.helpers.args import build_widget_args


def _powermenu_modal():
    def _inner():
        return run_shell_command("ebenezer ui powermenu")

    return _inner


def build_powermenu_widget(settings: AppSettings, kwargs: dict):
    """
    Build a power menu widget for the Qtile window manager.

    This function creates a TextBox widget configured with the provided settings
    and additional keyword arguments. The widget is intended to be used as a power
    menu, typically displaying a power icon and responding to mouse clicks to open
    a power menu modal.

    Args:
        settings (AppSettings): An instance of AppSettings containing configuration
                                for fonts, colors, and other settings.
        kwargs (dict): Additional keyword arguments to customize the widget.

    Returns:
        widget.TextBox: A configured TextBox widget for the power menu.
    """
    default_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "padding": 4,
        "foreground": settings.colors.fg_normal,
        "background": settings.colors.bg_topbar_arrow,
        "mouse_callbacks": {"Button1": _powermenu_modal()},
    }

    args = build_widget_args(
        settings,
        default_args,
        kwargs,
    )

    return widget.TextBox(args.pop("text", ""), **args)
