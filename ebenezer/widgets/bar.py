"""
This module provides functions to build a customized bar for the Qtile window manager
using various widgets defined in the ebenezer package.

Functions:
    build_bar(settings: AppSettings) -> bar.Bar:
        Constructs a bar with widgets specified in the settings.

    build_fallback_bar(settings: AppSettings) -> List[widget.base._Widget]:
        Constructs a fallback bar with a predefined set of widgets.

    _build_separator(_: AppSettings, args: dict) -> widget.Sep:
        Constructs a separator widget.

    _build_prompt(settings: AppSettings, kwargs: dict) -> widget.Prompt:
        Constructs a prompt widget with default and custom arguments.

    _build_task_list_widget(settings: AppSettings, args: dict) -> widget.TaskList:
        Constructs a task list widget.

    _build_widget(settings: AppSettings, widget_type: str, args: dict) -> widget.base._Widget:
        Constructs a widget based on the widget type and arguments provided.

    _build_widgets(settings: AppSettings) -> List[widget.base._Widget]:
        Constructs a list of widgets based on the settings.

Constants:
    WIDGETS (dict): A dictionary mapping widget types to their respective builder functions.
"""

from typing import Any, Callable, List

from libqtile import bar, widget
from libqtile.log_utils import logger

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.app_menu import build_app_menu_widget
from ebenezer.widgets.arrow import build_arrow_widget
from ebenezer.widgets.battery import build_battery_widget
from ebenezer.widgets.clock import build_clock_widget
from ebenezer.widgets.cpu import build_cpu_widget
from ebenezer.widgets.github import build_github_widget
from ebenezer.widgets.group_box import build_group_box
from ebenezer.widgets.helpers.args import build_widget_args
from ebenezer.widgets.hidden_tray import build_hidden_tray
from ebenezer.widgets.layout import build_current_layout_widget
from ebenezer.widgets.memory import build_memory_widget
from ebenezer.widgets.notification import build_notification_widget
from ebenezer.widgets.powermenu import build_powermenu_widget
from ebenezer.widgets.settings import build_settings_widget
from ebenezer.widgets.spacer import build_spacer_widget
from ebenezer.widgets.task_list import build_task_list_widget
from ebenezer.widgets.thermal import build_thermal_widget
from ebenezer.widgets.volume import build_volume_widget
from ebenezer.widgets.wallpaper import build_wallpaper_widget
from ebenezer.widgets.weather import build_weather_widget
from ebenezer.widgets.window_name import build_window_name_widget

CustomWidgets = dict[str, Callable[[AppSettings, dict], any]]


def build_bar(
    settings: AppSettings,
    custom_widgets: CustomWidgets = {},
):
    """
    Build and return a bar with the specified settings and custom widgets.

    Args:
        settings (AppSettings): The application settings containing bar configuration.
        custom_widgets (CustomWidgets, optional): A dictionary of custom widgets to include in the bar. Defaults to an empty dictionary.

    Returns:
        bar.Bar: The configured bar instance.
    """
    widgets = _build_widgets(settings, custom_widgets)

    return bar.Bar(
        widgets,
        settings.bar.size,
        background=settings.colors.bg_topbar,
        margin=settings.bar.margin,
    )


def build_fallback_bar(settings: AppSettings):
    return [
        build_group_box(settings, {}),
        _build_separator(settings, {}),
        _build_prompt(settings, {}),
        build_clock_widget(settings, {}),
        build_spacer_widget(settings, {}),
        build_current_layout_widget(settings, {}),
    ]


def _build_separator(_: AppSettings, args: dict):
    return widget.Sep(**args)


def _build_prompt(settings: AppSettings, kwargs: dict):
    default_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "foreground": settings.colors.fg_normal,
    }

    args = build_widget_args(
        settings,
        default_args,
        kwargs,
    )

    return widget.Prompt(**args)


def _build_task_list_widget(settings: AppSettings, args: dict):
    return build_task_list_widget(settings, args)


WIDGETS = {
    "arrow": build_arrow_widget,
    "app_menu": build_app_menu_widget,
    "battery": build_battery_widget,
    "clock": build_clock_widget,
    "cpu": build_cpu_widget,
    "current_layout": build_current_layout_widget,
    "github": build_github_widget,
    "group_box": build_group_box,
    "hidden_tray": build_hidden_tray,
    "memory": build_memory_widget,
    "notification": build_notification_widget,
    "powermenu": build_powermenu_widget,
    "separator": _build_separator,
    "settings": build_settings_widget,
    "spacer": build_spacer_widget,
    "prompt": _build_prompt,
    "task_list": _build_task_list_widget,
    "thermal": build_thermal_widget,
    "volume": build_volume_widget,
    "wallpaper": build_wallpaper_widget,
    "weather": build_weather_widget,
    "window_name": build_window_name_widget,
}


def _build_widget(
    settings: AppSettings,
    widget_type: str,
    args: dict,
    custom_widgets: CustomWidgets = {},
):
    builder = WIDGETS.get(widget_type) or custom_widgets.get(widget_type)

    if builder is None:
        return None

    return builder(settings, args)


def _build_widgets(
    settings: AppSettings,
    custom_widgets: CustomWidgets,
):
    try:
        widgets: List[Any] = []

        for config in settings.bar.widgets:
            next_widgets = _build_widget(
                settings, config.type, config.args, custom_widgets=custom_widgets
            )

            if next_widgets is None:
                logger.warning(
                    f"Widget {config.type} could not be found: {config.__dict__}"
                )
                continue
            elif isinstance(next_widgets, list):
                widgets = widgets + next_widgets
            else:
                widgets.append(next_widgets)

        return widgets
    except Exception as e:
        logger.warning("An error ocurred while trying to build bar", e, exc_info=True)
        return build_fallback_bar(settings)
