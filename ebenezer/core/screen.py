"""
screen.py
---------

This module provides functions to build screens for Qtile.

Functions:
    build_screen(settings: AppSettings) -> Screen:
        Builds a screen with a bar based on the provided settings.
"""

from libqtile.config import Screen

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.bar import CustomWidgets, build_bar


def build_screen(settings: AppSettings, custom_widgets: CustomWidgets = {}) -> Screen:
    """
    Builds a screen with a bar based on the provided settings.

    Args:
        settings (AppSettings): The application settings containing screen configurations.
        custom_widgets (CustomWidgets): The custom widgets to use in the bar

    Returns:
        Screen: The configured screen.
    """
    if settings.bar.position == "top":
        return Screen(top=build_bar(settings, custom_widgets))
    else:
        return Screen(bottom=build_bar(settings, custom_widgets))
