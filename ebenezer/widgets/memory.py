import psutil
from libqtile import widget
from libqtile.widget import Memory

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.formatter import burn_text
from ebenezer.widgets.helpers.args import build_widget_args


class ColorizedMemoryWidget(Memory):
    """
    A widget that displays memory usage with color-coded thresholds.

    Attributes:
        high_color (str): The color used when memory usage is above the high threshold.
        medium_color (str): The color used when memory usage is above the medium threshold but below the high threshold.
        default_color (str): The default color used when memory usage is below the medium threshold.
        threshold_medium (int): The memory usage percentage that triggers the medium color.
        threshold_high (int): The memory usage percentage that triggers the high color.

    Methods:
        __init__(**config):
            Initializes the ColorizedMemoryWidget with the given configuration.
        poll():
            Polls the current memory usage and updates the widget's display color based on the usage thresholds.
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
        mem = psutil.virtual_memory()
        text = Memory.poll(self).lstrip()

        if mem.percent > self.threshold_high:
            self.foreground = self.high_color
            text = burn_text(text)
        elif mem.percent > self.threshold_medium:
            self.foreground = self.medium_color
        else:
            self.foreground = self.default_color

        return text.strip()


def build_memory_widget(settings: AppSettings, kwargs: dict):
    """
    Build a memory widget for the Qtile status bar.

    This function creates a memory widget with customizable settings and arguments.
    It constructs the widget using the provided settings and additional keyword arguments.

    Args:
        settings (AppSettings): An instance of AppSettings containing configuration for fonts, colors, and monitoring thresholds.
        kwargs (dict): A dictionary of additional keyword arguments to customize the widget. It can contain:
            - "icon" (dict): Custom arguments for the icon part of the widget.
            - "sensor" (dict): Custom arguments for the memory sensor part of the widget.

    Returns:
        list: A list containing two elements:
            - widget.TextBox: A TextBox widget for the memory icon.
            - ColorizedMemoryWidget: A custom widget displaying memory usage with color thresholds.
    """
    default_icon_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "padding": 2,
        "foreground": settings.colors.fg_purple,
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
        "format": "{MemUsed: .0f}{mm}",
        "padding": 2,
        "foreground": settings.colors.fg_normal,
        "background": settings.colors.bg_topbar_arrow,
    }

    args = build_widget_args(
        settings,
        default_args,
        kwargs.get("sensor", {}),
    )

    return [
        widget.TextBox(f"{icon_args.pop("text", "󰄧")} ", **icon_args),
        ColorizedMemoryWidget(**args),
    ]
