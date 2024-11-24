from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.helpers.args import build_widget_args


def build_app_menu_widget(settings: AppSettings, kwargs: dict):
    """
    Build an application menu widget for the Qtile window manager.

    This function creates a TextBox widget with customizable settings and arguments.
    It uses default arguments for padding, font, fontsize, text when closed and open,
    and foreground color, which can be overridden by the provided kwargs.

    Args:
        settings (AppSettings): An instance of AppSettings containing configuration
                                for fonts and environment settings.
        kwargs (dict): Additional keyword arguments to customize the widget.

    Returns:
        widget.TextBox: A TextBox widget configured with the specified settings and arguments.
    """
    default_args = {
        "padding": 10,
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "text_closed": settings.environment.os_logo_icon,
        "text_open": settings.environment.os_logo_icon,
        "foreground": settings.environment.os_logo_icon_color,
    }

    args = build_widget_args(settings, default_args, kwargs)
    icon = kwargs.pop("icon", settings.environment.os_logo_icon)

    return widget.TextBox(f" {icon}", **args)
