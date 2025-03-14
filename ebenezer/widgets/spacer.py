from libqtile import bar, widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.helpers.args import build_widget_args


def build_spacer_widget(settings: AppSettings, kwargs: dict):
    """
    Build a spacer widget with specified settings.

    Args:
        _: AppSettings
            Placeholder for application settings, not used in the function.
        kwargs: dict
            Dictionary of keyword arguments to customize the spacer widget.

    Returns:
        widget.Spacer: A spacer widget instance with the specified settings.

    Notes:
        - The 'length' argument in kwargs can be "stretch", "calculated", or an integer.
        - If 'length' is "stretch", it will be set to bar.STRETCH.
        - If 'length' is "calculated", it will be set to bar.CALCULATED.
        - If 'length' is not an integer, it will default to 1.
    """
    default_args = {"length": bar.STRETCH}
    args = default_args | kwargs

    length = args.get("length")

    if length == "stretch":
        length = bar.STRETCH
    elif length == "calculated":
        length = bar.CALCULATED
    elif not isinstance(length, int):
        length = 1

    args["length"] = length
    args = build_widget_args(settings, default_args, args)

    return widget.Spacer(**args)
