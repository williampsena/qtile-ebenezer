from libqtile import widget
from libqtile.widget import CPU

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.formatter import burn_text
from ebenezer.widgets.helpers.args import build_widget_args


class ColorizedCPUWidget(CPU):
    """
    A widget that enhances the user experience by displaying CPU usage using color and icons.

    Attributes:
        high_color (str): The color used when CPU usage is above the high threshold.
        medium_color (str): The color used when CPU usage is above the medium threshold but below the high threshold.
        default_color (str): The default color used when CPU usage is below the medium threshold.
        threshold_medium (float): The CPU usage percentage that triggers the medium color.
        threshold_high (float): The CPU usage percentage that triggers the high color.

    Methods:
        __init__(**config):
            Initializes the ColorizedCPUWidget with the given configuration.

        poll():
            Polls the current CPU usage and updates the widget's display color based on the usage thresholds.
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
        text = CPU.poll(self)
        cpu = float(text.replace("%", ""))

        if cpu > self.threshold_high:
            self.foreground = self.high_color
            text = burn_text(text)
        elif cpu > self.threshold_medium:
            self.foreground = self.medium_color
        else:
            self.foreground = self.default_color

        return text


def build_cpu_widget(settings: AppSettings, kwargs: dict):
    """
    Build a CPU widget for the Qtile status bar.

    This function creates a CPU widget with customizable settings and arguments.
    It combines a text icon and a ColorizedCPUWidget to display CPU load information.

    Args:
        settings (AppSettings): An instance of AppSettings containing configuration settings.
        kwargs (dict): A dictionary of additional arguments to customize the widget.
            - "icon" (dict): Custom arguments for the icon TextBox widget.
            - "sensor" (dict): Custom arguments for the ColorizedCPUWidget.

    Returns:
        list: A list containing the TextBox widget for the icon and the ColorizedCPUWidget.
    """
    default_icon_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "padding": 2,
        "foreground": settings.colors.fg_yellow,
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
        "format": "{load_percent}% ",
        "padding": 2,
        "foreground": settings.colors.fg_normal,
        "background": settings.colors.bg_topbar_arrow,
    }

    args = build_widget_args(settings, default_args, kwargs.get("sensor", {}))

    return [
        widget.TextBox(f"{icon_args.pop("text", "")} ", **icon_args),
        ColorizedCPUWidget(**args),
    ]
