"""
keybindings.py
--------------

This module provides classes and functions to manage key bindings for Qtile.

Classes:
    AppSettingsKeyBinding:
        Manages individual key binding settings.

Functions:
    build_keybindings(items: List[dict]) -> List[AppSettingsKeyBinding]:
        Builds a list of key bindings from a list of dictionaries.
"""

from typing import List

from libqtile.log_utils import logger


class AppSettingsKeyBinding:
    name: str = ""
    keys: List[str] = []
    action: str = ""
    command: str = ""
    group: str = "custom"

    def __init__(self, **kwargs):
        """
        Initializes the AppSettingsKeyBinding with optional keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments to initialize the key binding settings.
        """
        self.name = kwargs.get("name", self.name)
        self.keys = kwargs.get("keys", "").split(" ")
        self.action = kwargs.get("action", self.action)
        self.command = kwargs.get("command", self.command)
        self.group = kwargs.get("group", self.group)


def build_keybindings(items: List[dict]) -> List[AppSettingsKeyBinding]:
    """
    Builds a list of key bindings from a list of dictionaries.

    Args:
        items (List[dict]): A list of dictionaries containing key binding configurations.

    Returns:
        List[AppSettingsKeyBinding]: A list of configured key bindings.
    """
    try:
        return [AppSettingsKeyBinding(**i) for i in items]
    except Exception as error:
        logger.warning(
            "An exception occurred while trying to build keybindings.",
            error,
            exc_info=True,
        )
        return []
