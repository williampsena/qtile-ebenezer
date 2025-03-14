from libqtile import bar, hook, widget
from libqtile.widget import base

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.helpers.args import build_widget_args


def get_layout_icon(layout_name):
    return ICONS.get(layout_name, "")


ICONS = {
    "bsp": "",
    "columns": "",
    "floating": "",
    "max": "",
    "matrix": "󰘨",
    "monadtall": "󰕴",
    "monadthreecol": "",
    "monadwide": "󰜩",
    "plasma": "",
    "ratiotile": "",
    "screensplit": "",
    "slice": "",
    "spiral": "",
    "stack": "",
    "tile": "",
    "treetab": "",
    "verticaltile": "",
    "zoomy": "",
}


class CurrentLayoutFontIcon(base._TextBox):
    """
    A widget that displays the current layout's icon in the bar.

    Attributes:
        text (str): The text to be displayed in the widget, which is the icon of the current layout.

    Methods:
        __init__(width=bar.CALCULATED, **config):
            Initializes the widget with the given width and configuration.

        _configure(qtile, bar):
            Configures the widget with the given Qtile instance and bar. Sets up the initial layout icon and hooks.

        hook_response(layout, group):
            Updates the widget's text with the new layout icon when the layout changes.

        setup_hooks():
            Subscribes to the layout_change hook to update the widget when the layout changes.

        remove_hooks():
            Unsubscribes from the layout_change hook.

        finalize():
            Cleans up by removing hooks and finalizing the base class.

        _fetch_icon(layout_name: str):
            Fetches the icon for the given layout name from the ICONS dictionary or returns the layout name if no icon is found.
    """

    def __init__(self, width=bar.CALCULATED, **config):
        base._TextBox.__init__(self, "", width, **config)

    def _configure(self, qtile, bar):
        base._TextBox._configure(self, qtile, bar)
        layout_id = self.bar.screen.group.current_layout
        self.text = self._fetch_icon(self.bar.screen.group.layouts[layout_id].name)
        self.setup_hooks()

        self.add_callbacks(
            {
                "Button1": qtile.next_layout,
                "Button2": qtile.prev_layout,
            }
        )

    def hook_response(self, layout, group):
        if group.screen is not None and group.screen == self.bar.screen:
            self.text = self._fetch_icon(layout.name)
            self.bar.draw()

    def setup_hooks(self):
        hook.subscribe.layout_change(self.hook_response)

    def remove_hooks(self):
        hook.unsubscribe.layout_change(self.hook_response)

    def finalize(self):
        self.remove_hooks()
        base._TextBox.finalize(self)

    def _fetch_icon(self, layout_name: str):
        layout_icon = ICONS.get(layout_name, layout_name)
        return f"{layout_icon} "


def build_current_layout_widget(settings: AppSettings, kwargs: dict):
    """
    Build a widget to display the current layout in Qtile.

    This function constructs a widget based on the provided settings and keyword arguments.
    It supports different types of widgets: text, icon, and a custom font icon.

    Args:
        settings (AppSettings): The application settings containing colors and fonts.
        kwargs (dict): Additional keyword arguments to customize the widget.

    Returns:
        widget: An instance of a Qtile widget to display the current layout.

    Raises:
        KeyError: If required keys are missing in the settings or kwargs.
        TypeError: If the provided arguments are of incorrect type.

    Example:
        settings = AppSettings()
        kwargs = {"widget_type": "text"}
        widget = build_current_layout_widget(settings, kwargs)
    """
    default_args = {
        "padding": 6,
        "scale": 0.6,
        "foreground": settings.colors.fg_normal,
        "background": settings.colors.bg_topbar_arrow,
        "font": settings.fonts.font_icon,
    }

    args = build_widget_args(settings, default_args, kwargs)
    type = kwargs.pop("widget_type", "font_icon")

    if type == "text":
        return widget.CurrentLayout(**args)
    elif type == "icon":
        return widget.CurrentLayoutIcon(**args)
    else:
        return CurrentLayoutFontIcon(**args)
