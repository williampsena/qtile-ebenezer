"""
groups.py
---------

This module provides functions to build groups and key bindings for Qtile.

Functions:
    build_groups(keys: List, settings: AppSettings):
        Builds groups and key bindings for Qtile based on the provided settings.
"""

from typing import List

from libqtile import qtile
from libqtile.config import DropDown, Group, Key, ScratchPad
from libqtile.lazy import lazy

from ebenezer.config.settings import AppSettings


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
                f"f{vt}",
                lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
                desc=f"Switch to VT{vt}",
            )
        )

    groups: list[any] = []

    for i, g in enumerate(settings.groups):
        key = g
        label = f"  {settings.groups[g].strip()}  "
        layout_default = settings.groups_layout.get("default", "monadtall")

        groups.append(
            Group(
                name=str(i + 1),
                layout=settings.groups_layout.get(key, layout_default),
                label=label,
            )
        )

    for g in groups:
        keys.extend(
            [
                # mod1 + letter of group = switch to group
                Key(
                    [mod],
                    g.name,
                    lazy.group[g.name].toscreen(0),
                    desc="Switch to group {}".format(g.name),
                ),
                # mod1 + shift + letter of group = move focused window to group
                Key(
                    [mod, "shift"],
                    g.name,
                    lazy.window.togroup(g.name, switch_group=False),
                    desc="Move focused window to group {}".format(g.name),
                ),
            ]
        )

    groups.extend(_build_scratchpad(settings))

    return groups, keys


def _build_scratchpad(settings: AppSettings) -> list[any]:
    if not settings.scratchpads or not settings.scratchpads.dropdowns:
        return []

    return [
        ScratchPad(
            "scratchpad",
            [
                DropDown(
                    name,
                    settings.commands.get(dropdown.command, dropdown.command),
                    **dropdown.args,
                )
                for name, dropdown in settings.scratchpads.dropdowns.items()
            ],
        )
    ]
