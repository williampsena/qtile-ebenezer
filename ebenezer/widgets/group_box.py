from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.helpers.args import build_widget_args


def build_group_box(settings: AppSettings, kwargs: dict):
    """
    Build a GroupBox widget with the specified settings and additional arguments.

    Args:
        settings (AppSettings): An instance of AppSettings containing configuration values.
        kwargs (dict): Additional keyword arguments to override default settings.

    Returns:
        widget.GroupBox: A configured GroupBox widget instance.

    The default arguments include:
        - margin_y (int): Vertical margin.
        - margin_x (int): Horizontal margin.
        - padding (int): Padding inside the widget.
        - borderwidth (int): Width of the border.
        - active (str): Color for active group.
        - inactive (str): Color for inactive group.
        - this_current_screen_border (str): Border color for the current screen's group.
        - this_screen_border (str): Border color for the screen's group.
        - other_current_screen_border (str): Border color for other screens' groups.
        - highlight_color (str): Color for highlighting.
        - highlight_method (str): Method of highlighting (e.g., "text").
        - font (str): Font used for the widget.
        - fontsize (int): Font size used for the widget.
        - foreground (str): Foreground color.
        - rounded (bool): Whether the corners are rounded.
        - urgent_alert_method (str): Method for urgent alerts (e.g., "border").
        - urgent_border (str): Border color for urgent alerts.

    The `build_widget_args` function is used to merge the default arguments with any
    additional arguments provided in `kwargs`.
    """
    default_args = {
        "margin_y": 3,
        "margin_x": 3,
        "padding": 1,
        "borderwidth": 2,
        "active": settings.colors.fg_normal,
        "inactive": settings.colors.fg_normal,
        "this_current_screen_border": settings.colors.bg_topbar_selected,
        "this_screen_border": settings.colors.fg_blue,
        "other_current_screen_border": settings.colors.bg_topbar_selected,
        "highlight_color": settings.colors.bg_topbar_selected,
        "highlight_method": "text",
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "foreground": settings.colors.fg_normal,
        "rounded": False,
        "urgent_alert_method": "border",
        "urgent_border": settings.colors.fg_urgent,
    }

    args = build_widget_args(
        settings,
        default_args,
        kwargs,
        [
            "active",
            "inactive",
            "this_current_screen_border",
            "this_screen_border",
            "other_current_screen_border",
            "highlight_color",
            "foreground",
            "urgent_border",
        ],
    )

    return widget.GroupBox(**args)
