from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.helpers.args import build_widget_args


def build_arrow_widget(settings: AppSettings, kwargs: dict):
    """
    Build an arrow widget for the Qtile bar.

    This function creates a TextBox widget with an arrow character, using the
    provided settings and additional keyword arguments.

    Args:
        settings (AppSettings): An instance of AppSettings containing configuration
                                for fonts and colors.
        kwargs (dict): Additional keyword arguments to customize the widget.

    Returns:
        widget.TextBox: A TextBox widget configured with the specified settings and arguments.
    """
    default_args = {
        "text": "",
        "font": settings.fonts.font_arrow,
        "fontsize": settings.fonts.font_arrow_size,
        "foreground": settings.colors.bg_topbar_arrow,
        "padding": 0,
    }

    args = build_widget_args(settings, default_args, kwargs)

    return widget.TextBox(**args)
