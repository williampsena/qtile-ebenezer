import subprocess

from libqtile.widget import base

from ebenezer.config.settings import AppSettings
from ebenezer.core.command import run_shell_command
from ebenezer.rofi.modals.confirm import confirm_cmd
from ebenezer.widgets.helpers.args import build_widget_args


def _notifications_actions():
    confirmed = confirm_cmd(
        "Confirm",
        "Would you like to clear notifications?",
    )

    if confirmed:
        run_shell_command("dunstctl history-clear")
    else:
        run_shell_command("dunstctl close-all")


class DunstWidget(base.ThreadPoolText):
    """
    A widget to display the count of notifications using dunst.

    Attributes:
        defaults (list): Default configuration options for the widget.
        count (int): The current count of notifications.
        animated (bool): Whether the bell icon should be animated.
        bells_index (int): Index to track the current bell icon.
        bells (list): List of bell icons.
        foreground_zero (str): Foreground color when there are no notifications.
        foreground_count (str): Foreground color when there are notifications.

    Methods:
        poll(): Updates the widget with the current notification count.
        get_bell_icon(): Returns the current bell icon based on the animation setting.
        get_notification_count(): Retrieves the current notification count from dunst.
        show_notifications(): Displays the notification history.
        clear_notifications(): Clears the notifications if there are any.
    """

    defaults = [
        ("update_interval", 3, "Interval to update the notification count"),
    ]

    def __init__(self, **config):
        super().__init__("", **config)

        settings = config.pop("settings")

        self.count = 0
        self.animated = config.get("animated", False)
        self.bells_index = 0
        self.bells = ["󰂚", "󰂞"]
        self.foreground_zero = config.get("foreground_zero", settings.colors.fg_normal)
        self.foreground_count = config.get(
            "foreground_count", settings.colors.fg_normal
        )

        self.add_defaults(DunstWidget.defaults)
        self.add_callbacks(
            {
                "Button1": self.show_notifications,
                "Button3": self.clear_notifications,
            }
        )

    def poll(self):
        self.count = self.get_notification_count()

        if self.count == 0:
            self.foreground = self.foreground_zero
            return ""
        else:
            bell_icon = self.get_bell_icon()
            self.foreground = self.foreground_count
            return f"{bell_icon} {self.count}"

    def get_bell_icon(self):
        if self.animated is False:
            return self.bells[0]

        self.bells_index = 1 if self.bells_index == 0 else 0
        return self.bells[self.bells_index]

    def get_notification_count(self):
        try:
            output = (
                subprocess.check_output(["dunstctl", "count"]).decode("utf-8").strip()
            )

            lines = output.splitlines()

            history_count = int(lines[2].split(":")[1].strip())

            return history_count
        except Exception:
            return 0

    def show_notifications(self):
        subprocess.Popen(["dunstctl", "history-pop"])

    def clear_notifications(self):
        if self.count == 0:
            return

        _notifications_actions()


def build_notification_widget(settings: AppSettings, kwargs: dict):
    """
    Build a notification widget with the given settings and additional arguments.

    Args:
        settings (AppSettings): The application settings containing fonts and colors.
        kwargs (dict): Additional keyword arguments to customize the widget.

    Returns:
        DunstWidget: An instance of the DunstWidget configured with the provided settings and arguments.

    The function initializes default arguments for the widget, including text, font, fontsize, padding, and colors.
    It then merges these default arguments with any additional arguments provided in kwargs, giving precedence to
    the values in kwargs. The resulting arguments are used to create and return a DunstWidget instance.
    """
    default_args = {
        "settings": settings,
        "default_text": "",
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "padding": 2,
        "foreground": settings.colors.fg_normal,
        "foreground_zero": settings.colors.fg_normal,
        "foreground_count": settings.colors.fg_yellow,
        "animated": False,
    }

    args = build_widget_args(
        settings,
        default_args,
        kwargs,
        ["foreground", "foreground_zero", "foreground_count"],
    )

    return DunstWidget(**args)
