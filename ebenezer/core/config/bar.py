"""
bar.py
------

This module provides classes to manage bar settings for Qtile.

Classes:
    AppSettingsBarWidget:
        Manages individual bar widget settings.

    AppSettingsBar:
        Manages bar settings including position, size, margin, and widgets.
"""

from typing import List


class AppSettingsBarWidget:
    type: str = ""
    args: dict = {}

    def __init__(self, **kwargs):
        """
        Initializes the AppSettingsBarWidget with optional keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments to initialize the bar widget settings.
        """
        self.type = kwargs.pop("type", self.type)
        self.args = kwargs


class AppSettingsBar:
    position: str = "top"
    size: int = 32
    margin: List[int] = [8, 8, 0, 8]
    widgets: List[AppSettingsBarWidget] = []

    def __init__(self, **kwargs):
        """
        Initializes the AppSettingsBar with optional keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments to initialize the bar settings.
        """
        self.position = kwargs.get("position", self.position)
        self.size = int(kwargs.get("size", str(self.size)))
        self.widgets = [AppSettingsBarWidget(**w) for w in kwargs.get("widgets", [])]

        margin = kwargs.get("margin")

        if margin:
            margin = margin.split(",")
            self.margin = [int(i) for i in margin]
