from libqtile import widget

from ebenezer.config.settings import AppSettings


def build_clock_widget(settings: AppSettings, kwargs: dict):
    """
    Build a clock widget with the given settings and additional arguments.

    Args:
        settings (AppSettings): The application settings containing fonts and colors.
        kwargs (dict): Additional keyword arguments to customize the clock widget.

    Returns:
        widget.Clock: A configured clock widget instance.
    """
    default_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "foreground": settings.colors.fg_normal,
        "padding": 2,
        "format": "%b %d, %I:%M %p",
    }

    args = default_args | kwargs

    return widget.Clock(**args)
