from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.core.command import lazy_command
from ebenezer.widgets.helpers.args import build_widget_args


def build_settings_widget(settings: AppSettings, kwargs: dict):
    """
    Build a settings widget for the ebenezer Qtile window manager.

    This function creates a TextBox widget that allows customization of the widget's appearance and behavior through the
    provided settings and additional keyword arguments.

    Args:
        settings (AppSettings): An instance of AppSettings containing configuration
                                for fonts, colors, and commands.
        kwargs (dict): Additional keyword arguments to customize the widget.

    Returns:
        widget.TextBox: A configured TextBox widget for displaying an icon and
                        handling mouse callbacks.
    """
    default_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "foreground": settings.colors.fg_normal,
        "background": settings.colors.bg_topbar_arrow,
        "mouse_callbacks": {"Button1": lazy_command("ebenezer ui settings")},
    }

    args = build_widget_args(
        settings,
        default_args,
        kwargs,
    )
    icon = kwargs.pop("icon", " ")

    return widget.TextBox(icon, **args)
