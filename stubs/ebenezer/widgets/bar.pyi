from _typeshed import Incomplete

from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.widgets.app_menu import build_app_menu_widget as build_app_menu_widget
from ebenezer.widgets.arrow import build_arrow_widget as build_arrow_widget
from ebenezer.widgets.battery import build_battery_widget as build_battery_widget
from ebenezer.widgets.clock import build_clock_widget as build_clock_widget
from ebenezer.widgets.cpu import build_cpu_widget as build_cpu_widget
from ebenezer.widgets.github import build_github_widget as build_github_widget
from ebenezer.widgets.group_box import build_group_box as build_group_box
from ebenezer.widgets.helpers.args import build_widget_args as build_widget_args
from ebenezer.widgets.hidden_tray import build_hidden_tray as build_hidden_tray
from ebenezer.widgets.layout import (
    build_current_layout_widget as build_current_layout_widget,
)
from ebenezer.widgets.memory import build_memory_widget as build_memory_widget
from ebenezer.widgets.notification import (
    build_notification_widget as build_notification_widget,
)
from ebenezer.widgets.powermenu import build_powermenu_widget as build_powermenu_widget
from ebenezer.widgets.spacer import build_spacer_widget as build_spacer_widget
from ebenezer.widgets.task_list import build_task_list_widget as build_task_list_widget
from ebenezer.widgets.thermal import build_thermal_widget as build_thermal_widget
from ebenezer.widgets.volume import build_volume_widget as build_volume_widget
from ebenezer.widgets.wallpaper import build_wallpaper_widget as build_wallpaper_widget
from ebenezer.widgets.weather import build_weather_widget as build_weather_widget
from ebenezer.widgets.window_name import (
    build_window_name_widget as build_window_name_widget,
)

def build_bar(settings: AppSettings): ...
def build_fallback_bar(settings: AppSettings): ...

WIDGETS: Incomplete
