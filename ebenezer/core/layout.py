"""
groups.py
---------

This module provides functions to build groups and key bindings for Qtile.

Functions:
    build_groups(keys: List, settings: AppSettings):
        Builds groups and key bindings for Qtile based on the provided settings.
"""

from typing import Any, Callable, Dict

from libqtile import layout, qtile
from libqtile.config import Match
from libqtile.layout.base import Layout as BaseLayout
from libqtile.log_utils import logger

from ebenezer.config.settings import AppSettings, load_settings_by_files

"""
CENTER_WINDOWS_TITLES
---------------------

A list of predefined window titles used to identify specific windows for centralization.

This list contains titles of windows that should be centralized on the screen when they
are opened. The titles are case-insensitive and are matched against the 'name' attribute
of the window object.

Example:
    CENTER_WINDOWS_TITLES = ["ebenezer - configuration manager"]
"""
CENTER_WINDOWS_TITLES = ["ebenezer - configuration manager"]

"""
LAYOUTS
-------

A dictionary mapping layout names to their corresponding layout creation functions.

Each key in the dictionary represents a layout name (e.g., "bsp", "columns", "floating"),
and the value is a lambda function that takes two arguments:
    - settings: An instance of AppSettings containing configuration details.
    - args: A dictionary of additional arguments to customize the layout.

The lambda function returns an instance of the corresponding layout class from libqtile.

Supported Layouts:
    - bsp: Binary Space Partitioning layout.
    - columns: Columns layout.
    - floating: Floating layout with customizable float rules.
    - max: Maximized layout with no borders or margins.
    - matrix: Matrix layout.
    - monadtall: MonadTall layout.
    - monadthreecol: MonadThreeCol layout.
    - monadwide: MonadWide layout.
    - plasma: Plasma layout.
    - ratiotile: RatioTile layout.
    - screensplit: ScreenSplit layout.
    - slice: Slice layout.
    - spiral: Spiral layout.
    - stack: Stack layout.
    - tile: Tile layout with customizable shift_windows, border_width, margin, and ratio.
    - treetab: TreeTab layout.
    - verticaltile: VerticalTile layout.
    - zoomy: Zoomy layout.
"""
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
        "border_width": 2,
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
    """
    Sets the given window to floating mode if it matches any of the predefined rules.

    The function retrieves floating window rules from the settings and checks if the
    provided window matches any of these rules. If a match is found, the window is
    set to floating mode.

    Args:
        window: The window object to be checked and potentially set to floating mode.

    Rules:
        - Matches are determined based on `wm_class` and `title` attributes of the window.
        - The rules are loaded from the `floating` section of the settings, which
          contains lists of `wm_class` and `title` values to match against.

    Note:
        This function assumes the existence of a `load_settings_by_files` function
        to retrieve settings and a `Match` class to define matching rules.
    """
    """"""
    settings = load_settings_by_files()

    rules = [
        *[Match(wm_class=f) for f in settings.floating.get("wm_class", [])],
        *[Match(title=f) for f in settings.floating.get("title", [])],
    ]

    for rule in rules:
        if window.match(rule):
            window.floating = True


def centralize_window(settings: AppSettings, window):
    """
    Adjusts the size and position of a floating window to centralize it on the screen.

    If the window is floating, it resizes the window to 80% of the screen's width and height,
    places it at the center of the screen, and applies a border with the active border color.

    Args:
        settings (AppSettings): An instance of AppSettings containing configuration details.
        window: The window object to be centralized. It is expected to have attributes like
                'floating', 'place', and 'center'.

    Returns:
        None
    """
    if window.floating:
        width = int(qtile.current_screen.width * 0.8)
        height = int(qtile.current_screen.height * 0.8)

        window.place(
            x=0,
            y=0,
            width=width,
            height=height,
            borderwidth=1,
            bordercolor=settings.colors.border_color_active,
        )
        window.center()


def is_ebenezer_window(window):
    """
    Determines if a given window matches any of the predefined titles in CENTER_WINDOWS_TITLES.

    Args:
        window: An object representing a window, which is expected to have a 'name' attribute.

    Returns:
        bool: True if the window's name contains any of the titles in CENTER_WINDOWS_TITLES (case-insensitive),
        otherwise False.
    """
    return any(title.lower() in window.name.lower() for title in CENTER_WINDOWS_TITLES)
