#!/usr/bin/env python3

import importlib.resources as pkg_resources
import subprocess

from ebenezer.config.settings import load_settings_by_files


def _rofi_command(theme, prompt, message=None):
    command = ["rofi", "-theme", theme, "-dmenu", "-p", prompt]
    if message:
        command.extend(["-mesg", message])
    return command


def _confirm_cmd():
    confirm_theme = pkg_resources.files("ebenezer.rofi.modals").joinpath("confirm.rasi")
    command = _rofi_command(str(confirm_theme), "Confirmation", "Are you sure?")
    command.extend(
        [
            "-theme-str",
            "window {location: center; anchor: center; fullscreen: false; width: 350px;}",
            "-theme-str",
            'mainbox {orientation: vertical; children: [ "message", "listview" ];}',
            "-theme-str",
            "listview {columns: 2; lines: 1;}",
            "-theme-str",
            "element-text {horizontal-align: 0.5;}",
            "-theme-str",
            "textbox {horizontal-align: 0.5;}",
        ]
    )
    return (
        subprocess.run(command, stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
    )


def _confirm_exit():
    yes = "󰩐"
    return _confirm_cmd().strip() == yes


def _shutdown():
    if _confirm_exit():
        subprocess.run(["systemctl", "poweroff"])


def _reboot():
    if _confirm_exit():
        subprocess.run(["systemctl", "reboot"])


def _suspend():
    subprocess.run(["amixer", "set", "Master", "mute"])
    subprocess.run(["systemctl", "suspend"])


def _lock_screen():
    settings = load_settings_by_files()
    _close_rofi()
    subprocess.run(settings.lock_screen.command, shell=True)


def _logout():
    subprocess.run(["qtile", "cmd-obj", "-o", "cmd", "-f", "shutdown"])


def _close_rofi():
    subprocess.run(["pkill", "^rofi"])
    subprocess.run(["sleep", "0.5"])


def main():
    uptime = (
        subprocess.run(["uptime", "-p"], stdout=subprocess.PIPE)
        .stdout.decode("utf-8")
        .strip()
        .replace("up ", "")
    )

    rofi_theme = pkg_resources.files("ebenezer.rofi.powermenu").joinpath(
        "powermenu.rasi"
    )
    rofi_cmd = _rofi_command(rofi_theme, f"Uptime: {uptime}")

    options = {
        "󰐥": _shutdown,
        "": _reboot,
        "": _lock_screen,
        "": _suspend,
        "󰍃": _logout,
    }

    chosen = (
        subprocess.run(
            rofi_cmd,
            input="\n".join(options.keys()).encode(),
            stdout=subprocess.PIPE,
        )
        .stdout.decode("utf-8")
        .strip()
    )
    if chosen in options:
        options[chosen]()


if __name__ == "__main__":
    main()
