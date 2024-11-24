from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.helpers.args import build_widget_args


def build_window_name_widget(settings: AppSettings, kwargs: dict):
    """
    Build a WindowName widget with the specified settings and additional arguments.

    Args:
        settings (AppSettings): The application settings containing fonts and colors.
        kwargs (dict): Additional keyword arguments to customize the widget.

    Returns:
        widget.WindowName: A configured WindowName widget instance.

    The function uses default arguments for font, fontsize, foreground color, and max_chars,
    which can be overridden by the provided kwargs. The 'foreground' key is explicitly
    allowed to be overridden.
    """
    default_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "foreground": settings.colors.fg_normal,
        "max_chars": 30,
    }

    args = build_widget_args(
        settings,
        default_args,
        kwargs,
        [
            "foreground",
        ],
    )

    return widget.WindowName(**args)
