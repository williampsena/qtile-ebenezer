from _typeshed import Incomplete
from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.widgets.formatter import burn_text as burn_text
from ebenezer.widgets.helpers.args import build_widget_args as build_widget_args
from libqtile.widget import ThermalSensor

class ColorizedThermalWidget(ThermalSensor):
    high_color: Incomplete
    medium_color: Incomplete
    default_color: Incomplete
    threshold_medium: Incomplete
    threshold_high: Incomplete
    def __init__(self, **config) -> None: ...
    foreground: Incomplete
    def poll(self): ...

def build_thermal_widget(settings: AppSettings, kwargs: dict): ...
