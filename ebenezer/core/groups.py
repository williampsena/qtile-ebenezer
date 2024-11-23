"""
groups.py
---------

This module provides functions to build groups and key bindings for Qtile.

Functions:
    build_groups(keys: List, settings: AppSettings):
        Builds groups and key bindings for Qtile based on the provided settings.
"""

from typing import List

from libqtile.config import Key
from libqtile.lazy import lazy

from ebenezer.core.config.settings import AppSettings


def build_groups(keys: List, settings: AppSettings):
    """
    Builds groups and key bindings for Qtile based on the provided settings.

    Args:
        keys (List): The list of key bindings to be extended.
        settings (AppSettings): The application settings containing environment configurations.
    """
    mod = settings.environment.modkey

    # Add key bindings to switch VTs in Wayland.
    # We can't check qtile.core.name in default config as it is loaded before qtile is started
    # We therefore defer the check until the key binding is run by using .when(func=...)
    for vt in range(1, 8):
        keys.append(
            Key(
                ["control", "mod1"],
                str(vt),
                lazy.spawn(f"chvt {vt}"),
                desc=f"Switch to virtual terminal {vt}",
            )
        )

    # Additional group and key binding logic can be added here
