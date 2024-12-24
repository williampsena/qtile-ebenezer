#!/usr/bin/env python3

import importlib.resources as pkg_resources
import subprocess

from ebenezer.rofi.modals.confirm import confirm_cmd


def _rofi_command(theme, prompt, message=None):
    command = ["rofi", "-theme", theme, "-dmenu", "-p", prompt]
    if message:
        command.extend(["-mesg", message])
    return command


def _confirm_cmd() -> bool:
    return confirm_cmd("Confirmation", "Are you sure?")


def _confirm_exit() -> bool:
    return _confirm_cmd()


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
    _close_rofi()
    subprocess.Popen(["ebenezer", "ui", "lock"])


def _logout():
    return subprocess.Popen(["qtile", "cmd-obj", "-o", "cmd", "-f", "shutdown"])


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
        options[chosen.strip()]()
    else:
        print("⚠️ Oh no! Invalid choice.")


if __name__ == "__main__":
    main()
