from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.helpers.args import build_widget_args


def build_battery_widget(settings: AppSettings, kwargs: dict):
    """
    Build a battery widget with the specified settings and additional arguments.

    Args:
        settings (AppSettings): An instance of AppSettings containing configuration for fonts, colors, etc.
        kwargs (dict): Additional keyword arguments to customize the widget.

    Returns:
        widget.Battery: A configured Battery widget instance.
    """
    default_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "format": "{char} {percent:2.0%}",
        "charge_char": "",
        "discharge_char": " ",
        "empty_char": " ",
        "full_char": " ",
        "not_charging_char": "󰚦",
        "unknown_char": "󰛄 ",
        "foreground": settings.colors.fg_normal,
        "padding": 5,
        "background": settings.colors.bg_topbar_arrow,
    }

    args = build_widget_args(settings, default_args, kwargs)

    return widget.Battery(**args)
