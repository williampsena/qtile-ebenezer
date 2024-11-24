import re

import psutil
from libqtile import widget
from libqtile.widget import ThermalSensor

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.formatter import burn_text
from ebenezer.widgets.helpers.args import build_widget_args


class ColorizedThermalWidget(ThermalSensor):
    """
    A widget that enhances the user experience by displaying thermal sensors using color and icons.

    Attributes:
        high_color (str): The color used when the temperature exceeds the high threshold.
        medium_color (str): The color used when the temperature exceeds the medium threshold but is below the high threshold.
        default_color (str): The default color used when the temperature is below the medium threshold.
        threshold_medium (float): The temperature threshold for medium level.
        threshold_high (float): The temperature threshold for high level.

    Methods:
        poll() -> str:
            Retrieves the current temperature, updates the foreground color based on the temperature thresholds,
            and returns the temperature text, potentially modified with an icon.
    """

    def __init__(self, **config):
        settings = config.pop("settings")
        super().__init__(**config)

        self.high_color = settings.colors.get_color(settings.monitoring.high_color)
        self.medium_color = settings.colors.get_color(settings.monitoring.medium_color)
        self.default_color = settings.colors.get_color(
            settings.monitoring.default_color
        )
        self.threshold_medium = config.get(
            "threshold_medium", settings.monitoring.threshold_medium
        )
        self.threshold_high = config.get(
            "threshold_high", settings.monitoring.threshold_high
        )

    def poll(self):
        text = ThermalSensor.poll(self)
        temperature = float(re.sub(r"\D", "", text))

        if temperature > self.threshold_high:
            self.foreground = self.high_color
            text = burn_text(text)
        elif temperature > self.threshold_medium:
            self.foreground = self.medium_color
        else:
            self.foreground = self.default_color

        return text


def build_thermal_widget(settings: AppSettings, kwargs: dict):
    """
    Build a thermal widget for monitoring temperature.

    This function creates a thermal widget with customizable settings and arguments.
    It constructs the widget using default and provided arguments for icon and sensor.

    Args:
        settings (AppSettings): The application settings containing fonts, colors, and monitoring thresholds.
        kwargs (dict): Additional keyword arguments to customize the widget. It can contain:
            - "icon" (dict): Custom arguments for the icon widget.
            - "sensor" (dict): Custom arguments for the sensor widget.

    Returns:
        list: A list containing the icon widget and the thermal sensor widget.
    """
    default_icon_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "padding": 2,
        "foreground": settings.colors.fg_light_blue,
        "background": settings.colors.bg_topbar_arrow,
    }

    icon_args = build_widget_args(
        settings,
        default_icon_args,
        kwargs.get("icon", {}),
    )

    default_args = {
        "settings": settings,
        "threshold_medium": settings.monitoring.threshold_medium,
        "threshold_high": settings.monitoring.threshold_high,
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "format": "{temp:.0f}{unit} ",
        "padding": 2,
        "foreground": settings.colors.fg_normal,
        "foreground_alert": settings.colors.fg_normal,
        "background": settings.colors.bg_topbar_arrow,
    }

    args = build_widget_args(
        settings,
        default_args,
        kwargs.get("sensor", {}),
        ["foreground", "foreground_alert", "background"],
    )

    return [
        widget.TextBox(icon_args.pop("text", "󱃂"), **icon_args),
        ColorizedThermalWidget(**args),
    ]


def _get_temperature():
    temperatures = psutil.sensors_temperatures()

    if "coretemp" in temperatures:
        core0_temp = next(
            (temp for temp in temperatures["coretemp"] if temp.label == "Core 0"), None
        )

        if core0_temp:
            return float(core0_temp.current)
        else:
            return 0
    else:
        return 0
