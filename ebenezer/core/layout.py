"""
groups.py
---------

This module provides functions to build groups and key bindings for Qtile.

Functions:
    build_groups(keys: List, settings: AppSettings):
        Builds groups and key bindings for Qtile based on the provided settings.
"""

from typing import Any, Callable, Dict

from libqtile import layout
from libqtile.config import Match
from libqtile.layout.base import Layout as BaseLayout
from libqtile.log_utils import logger

from ebenezer.config.settings import AppSettings, load_settings_by_files

LAYOUTS: Dict[str, Callable[[AppSettings, Dict[str, Any]], BaseLayout]] = {
    "bsp": lambda _, args: layout.Bsp(**args),
    "columns": lambda _, args: layout.Columns(**args),
    "floating": lambda settings, args: layout.Floating(
        **args,
        float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
            *layout.Floating.default_float_rules,
            Match(wm_class="pavucontrol"),  # gitk
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry,
        ]
        + [Match(title=f) for f in settings.floating.get("wm_class", [])]
        + [Match(wm_class=f) for f in settings.floating.get("title", [])],
    ),
    "max": lambda _, args: layout.Max(**({"border_width": 0, "margin": 0} | args)),
    "matrix": lambda _, args: layout.Matrix(**args),
    "monadtall": lambda _, args: layout.MonadTall(**args),
    "monadthreecol": lambda _, args: layout.MonadThreeCol(**args),
    "monadwide": lambda _, args: layout.MonadWide(**args),
    "plasma": lambda _, args: layout.Plasma(**args),
    "ratiotile": lambda _, args: layout.RatioTile(**args),
    "screensplit": lambda _, args: layout.ScreenSplit(**args),
    "slice": lambda _, args: layout.Slice(**args),
    "spiral": lambda _, args: layout.Spiral(**args),
    "stack": lambda _, args: layout.Stack(**args),
    "tile": lambda _, args: layout.Tile(
        **(
            {
                "shift_windows": True,
                "border_width": 0,
                "margin": 0,
                "ratio": 0.335,
            }
            | args
        )
    ),
    "treetab": lambda _, args: layout.TreeTab(**args),
    "verticaltile": lambda _, args: layout.VerticalTile(**args),
    "zoomy": lambda _, args: layout.Zoomy(**args),
}


def build_layouts(settings: AppSettings):
    """
    Build a list of layout instances based on the provided settings.

    Args:
        settings (AppSettings): An instance of AppSettings containing layout configurations.

    Returns:
        list: A list of layout instances created based on the settings.
    """
    ""
    layouts = []

    default_args = {
        "border_width": 4,
        "margin": 8,
        "border_focus": settings.colors.border_color_normal,
        "border_normal": settings.colors.border_color_active,
    }

    for _, l in enumerate(settings.layouts):
        fn_layout = LAYOUTS.get(l)

        if not fn_layout:
            logger.warning(f"Unknown layout: {l}")
            continue

        layouts.append(fn_layout(settings, default_args | settings.layouts.get(l, {})))

    return layouts


def set_floating_window(window):
    settings = load_settings_by_files()

    rules = [
        *[Match(wm_class=f) for f in settings.floating.get("wm_class", [])],
        *[Match(title=f) for f in settings.floating.get("title", [])],
    ]

    for rule in rules:
        if window.match(rule):
            window.floating = True
