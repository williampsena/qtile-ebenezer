"""
keys.py
-------

This module provides functions to build key bindings for Qtile.

Functions:
    _build_key_spawn(settings: AppSettings, binding: AppSettingsKeyBinding):
        Builds a key binding for spawning a command based on the provided settings and key binding configuration.

    _build_key_spawn_command(settings: AppSettings, binding: AppSettingsKeyBinding):
        Builds a key binding for spawning a command from the settings commands based on the provided settings and key binding configuration.

    build_keys(settings: AppSettings) -> List[Any]:
        Builds a list of key bindings based on the provided settings.

    _build_keys_from_config(settings: AppSettings, keys: List[Any]) -> List[Any]:
        Builds key bindings from the configuration and appends them to the provided keys list.
"""

import io
import os
import shutil
from collections import defaultdict
from typing import Any, Dict, List, NamedTuple

from colorama import Back, Fore, Style, init
from libqtile.config import Key
from libqtile.lazy import lazy

from ebenezer.config.keybindings import AppSettingsKeyBinding
from ebenezer.config.settings import AppSettings, load_settings_by_files
from ebenezer.core.command import lazy_spawn
from ebenezer.widgets.backlight import setup_backlight_keys
from ebenezer.widgets.volume import setup_volume_keys


class ColorKeybindingGroup(NamedTuple):
    name: str
    foreground_ansi: str = ""
    background_ansi: str = ""
    foreground: str = ""
    background: str = ""


COLOR_KEYBINDING_GROUPS = {
    "apps": ColorKeybindingGroup(
        "󰀻  apps", Fore.GREEN, Back.BLACK, "#00FF00", "#000000"
    ),
    "window": ColorKeybindingGroup(
        "  window", Fore.CYAN, Back.BLACK, "#00FFFF", "#000000"
    ),
    "custom": ColorKeybindingGroup(
        "󱡄 custom", Fore.WHITE, Back.MAGENTA, "#FFFFFF", "#FF00FF"
    ),
    "laucher": ColorKeybindingGroup(
        "󱓞 laucher", Fore.RED, Back.BLACK, "#FF0000", "#000000"
    ),
    "layout": ColorKeybindingGroup(
        "  layout", Fore.MAGENTA, Back.BLACK, "#FF00FF", "#000000"
    ),
    "media": ColorKeybindingGroup(
        "  media", Fore.YELLOW, Back.BLACK, "#FFFF00", "#000000"
    ),
    "qtile": ColorKeybindingGroup(
        "  qtile", Fore.BLUE, Back.BLACK, "#0000FF", "#000000"
    ),
    "screen": ColorKeybindingGroup(
        "󰍹  screen", Fore.WHITE, Back.BLACK, "#FFFFFF", "#000000"
    ),
    "screenshot": ColorKeybindingGroup(
        "  screenshot", Fore.YELLOW, Back.BLACK, "#FFFF00", "#000000"
    ),
    "settings": ColorKeybindingGroup(
        "  settings", Fore.BLACK, Back.GREEN, "#000000", "#00FF00"
    ),
}


def _build_key_spawn(settings: AppSettings, binding: AppSettingsKeyBinding):
    """
    Builds a key binding for spawning a command based on the provided settings and key binding configuration.

    Args:
        settings (AppSettings): The application settings containing environment configurations.
        binding (AppSettingsKeyBinding): The key binding configuration.

    Returns:
        Key: The configured key binding for spawning the command.
    """
    return _build_key(
        _format_keybinding(settings, binding.keys),
        lazy_spawn(binding.command),
    )


def _build_key_spawn_command(settings: AppSettings, binding: AppSettingsKeyBinding):
    cmd = settings.commands.get(binding.command)

    if cmd is None:
        return None

    return _build_key(
        _format_keybinding(settings, binding.keys),
        lazy_spawn(cmd),
    )


def _build_key_spawn_terminal(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys),
        lazy_spawn(settings.environment.terminal),
    )


def _build_key_spawn_browser(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys),
        lazy.spawn(settings.environment.browser),
    )


def _build_key_lock_screen(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys),
        lazy.spawn(os.path.expanduser(settings.lock_screen.command)),
    )


def _build_key_next_layout(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.next_layout())


def _build_key_kill_window(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.window.kill())


def _build_key_reload_config(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.reload_config())


def _build_key_shutdown(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.shutdown())


def _build_key_spawn_cmd(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.spawncmd())


def _build_key_focus_left(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.layout.left())


def _build_key_focus_right(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.layout.right())


def _build_key_focus_down(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.layout.down())


def _build_key_focus_up(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.layout.up())


def _build_key_focus_next(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.layout.next())


def _build_key_fullscreen(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.window.toggle_fullscreen()
    )


def _build_key_floating(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.window.toggle_floating()
    )


def _build_key_shuffle_left(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.layout.shuffle_left()
    )


def _build_key_shuffle_right(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.layout.shuffle_right()
    )


def _build_key_shuffle_down(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.layout.shuffle_down()
    )


def _build_key_shuffle_up(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.layout.shuffle_up()
    )


def _build_key_grow_left(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.layout.grow_left()
    )


def _build_key_grow_right(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.layout.grow_right()
    )


def _build_key_grow_down(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.layout.grow_down()
    )


def _build_key_grow_up(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.layout.grow_up())


def _build_key_reset_windows(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.layout.normalize()
    )


def _build_key_toggle_group(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.group.toggle_groups()
    )


def _build_key_next_screen(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.next_screen())


def _build_key_previous_screen(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.previous_screen()
    )


def _build_key_first_screen(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.to_screen(0))


def _build_key_second_screen(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.to_screen(1))


def _build_key_dropdown(settings: AppSettings, binding: AppSettingsKeyBinding):
    """
    Builds a key binding for toggling a dropdown terminal based on the provided settings and key binding configuration.

    Args:
        settings (AppSettings): The application settings containing environment configurations.
        binding (AppSettingsKeyBinding): The key binding configuration.

    Returns:
        Key: The configured key binding for toggling the dropdown terminal.
    """
    dropdown = settings.scratchpads.dropdowns.get(binding.command)

    if dropdown is None:
        return None

    return _build_key(
        _format_keybinding(settings, binding.keys),
        lazy.group["scratchpad"].dropdown_toggle(dropdown.name),
    )


ACTIONS = {
    "browser": _build_key_spawn_browser,
    "cmd": _build_key_spawn_cmd,
    "dropdown": _build_key_dropdown,
    "first_screen": _build_key_first_screen,
    "floating": _build_key_floating,
    "focus_down": _build_key_focus_down,
    "focus_left": _build_key_focus_left,
    "focus_next": _build_key_focus_next,
    "focus_right": _build_key_focus_right,
    "focus_up": _build_key_focus_up,
    "fullscreen": _build_key_fullscreen,
    "grow_down": _build_key_grow_down,
    "grow_left": _build_key_grow_left,
    "grow_right": _build_key_grow_right,
    "grow_up": _build_key_grow_up,
    "kill_window": _build_key_kill_window,
    "lock_screen": _build_key_lock_screen,
    "next_layout": _build_key_next_layout,
    "next_screen": _build_key_next_screen,
    "previous_screen": _build_key_previous_screen,
    "reload_config": _build_key_reload_config,
    "reset_windows": _build_key_reset_windows,
    "second_screen": _build_key_second_screen,
    "shuffle_down": _build_key_shuffle_down,
    "shuffle_left": _build_key_shuffle_left,
    "shuffle_right": _build_key_shuffle_right,
    "shuffle_up": _build_key_shuffle_up,
    "shutdown": _build_key_shutdown,
    "spawn_command": _build_key_spawn_command,
    "spawn": _build_key_spawn,
    "terminal": _build_key_spawn_terminal,
    "toggle_group": _build_key_toggle_group,
}


def build_keys(settings: AppSettings):
    """
    Builds a list of key bindings based on the provided settings.

    Args:
        settings (AppSettings): The application settings containing key binding configurations.

    Returns:
        List[Any]: The list of configured key bindings.
    """
    keys = setup_volume_keys(settings) + setup_backlight_keys()

    keys = _build_keys_from_config(settings, keys)

    return keys


def _build_keys_from_config(settings: AppSettings, keys: List[Any]):
    """
    Builds key bindings from the configuration and appends them to the provided keys list.

    Args:
        settings (AppSettings): The application settings containing key binding configurations.
        keys (List[Any]): The list of existing key bindings to be extended.

    Returns:
        List[Any]: The extended list of key bindings.
    """
    for binding in settings.keybindings:
        action_callable = ACTIONS.get(binding.action)
        key = None

        if action_callable:
            key = action_callable(settings, binding)

        if key:
            keys.append(key)

    return keys


def _build_key(keybinding: List[str], command):
    """
    Builds a key binding with the given key combination and command.

    Args:
        key_combination (List[str]): The key combination for the binding.
        command (Any): The command to be executed.

    Returns:
        Key: The configured key binding.
    """
    return Key(
        keybinding[:-1],
        keybinding[-1],
        command,
    )


def _format_keybinding(settings: AppSettings, keys: List[str]):
    """
    Formats the key binding by replacing placeholders with actual values.

    Args:
        settings (AppSettings): The application settings containing environment configurations.
        keys (List[str]): The list of keys for the binding.

    Returns:
        List[str]: The formatted key binding.
    """
    return [k.replace("$mod", settings.environment.modkey) for k in keys]


def _format_keybinding_icon(settings: AppSettings, keys: List[str]) -> str:
    """
    Formats the key binding by replacing placeholders with actual values.

    Args:
        keybinding (str): The key binding to be formatted.

    Returns:
        str: The formatted key binding.
    """

    keybinding = " + ".join(_format_keybinding(settings, keys))

    return (
        keybinding.lower()
        .replace("mod4", "  mod4")
        .replace("return", "󰌑 enter")
        .replace("shift", "󰘶 shift")
        .replace("tab", " tab")
    )


def fetch_keybindings_text(settings: AppSettings | None = None) -> str:
    settings = settings or load_settings_by_files()
    init(autoreset=True)
    print("\033c", end="")
    print(f"🪨  {Fore.LIGHTBLUE_EX}ebenezer keybindings{Style.RESET_ALL}\n")

    grouped_keybindings: Dict[str, List[AppSettingsKeyBinding]] = defaultdict(list)

    for binding in settings.keybindings:
        grouped_keybindings[binding.group].append(binding)

    columns, _ = shutil.get_terminal_size()

    if columns < 100:
        return _fetch_keybindings_text_single(settings, grouped_keybindings)
    else:
        return _fetch_keybindings_text_column(settings, grouped_keybindings)


def _fetch_keybindings_text_single(
    settings: AppSettings, grouped_keybindings: Dict[str, List[AppSettingsKeyBinding]]
) -> str:
    buffer = io.StringIO()

    for binding in settings.keybindings:
        grouped_keybindings[binding.group].append(binding)

    for group, bindings in grouped_keybindings.items():
        group_settings = COLOR_KEYBINDING_GROUPS.get(
            group, COLOR_KEYBINDING_GROUPS.get("custom")
        )

        buffer.write(
            f"{group_settings.foreground_ansi}{group_settings.background_ansi} {group_settings.name} {Style.RESET_ALL}\n\n"
        )

        for binding in bindings:
            keys = _format_keybinding_icon(settings, binding.keys)
            buffer.write(f"  {Fore.LIGHTBLACK_EX}{keys}  {Fore.WHITE}{binding.name}\n")

        buffer.write("\n")

    return buffer.getvalue()


def _fetch_keybindings_text_column(
    settings: AppSettings, grouped_keybindings: Dict[str, List[AppSettingsKeyBinding]]
) -> str:

    left_column = []
    right_column = []
    max_text_from_left = 0

    for i, (group, bindings) in enumerate(
        sorted(grouped_keybindings.items(), key=lambda item: len(item[1]), reverse=True)
    ):
        group_settings = COLOR_KEYBINDING_GROUPS.get(
            group, COLOR_KEYBINDING_GROUPS.get("custom")
        )

        group_header = f"{group_settings.foreground_ansi}{group_settings.background_ansi} {group_settings.name} {Style.RESET_ALL}\n\n"

        if i % 2 == 0:
            left_column.append(group_header)
        else:
            right_column.append(group_header)

        for binding in bindings:
            keys = _format_keybinding_icon(settings, binding.keys)
            binding_text = f"  {Fore.LIGHTBLACK_EX}{keys}  {Fore.WHITE}{binding.name}\n"

            if i % 2 == 0:
                max_text_from_left = max(max_text_from_left, len(binding_text))
                left_column.append(binding_text)
            else:
                right_column.append(binding_text)

        if i % 2 == 0:
            left_column.append("\n")
        else:
            right_column.append("\n")

    colspan = f"\033[{max_text_from_left}G"
    right_column = [f"{colspan}{text}" for text in right_column]

    left_column_text = "".join(left_column)
    right_column_text = "".join(right_column)

    left_lines = left_column_text.splitlines()
    right_lines = right_column_text.splitlines()
    max_lines = max(len(left_lines), len(right_lines))

    combined_lines = []
    for i in range(max_lines):
        left_line = left_lines[i] if i < len(left_lines) else ""
        right_line = right_lines[i] if i < len(right_lines) else ""
        combined_lines.append(f"{left_line:<40} {right_line}")

    return "\n".join(combined_lines)
