#!/usr/bin/env python3

import importlib.resources as pkg_resources
import subprocess

YES_LABEL = "󰩐"
NO_LABEL = ""


def confirm_cmd(title, question) -> bool:
    theme = pkg_resources.files("ebenezer.rofi.modals").joinpath("confirm.rasi")
    command = [
        "rofi",
        "-dmenu",
        "-p",
        title,
        "-mesg",
        question,
        "-theme",
        theme,
    ]

    result = (
        subprocess.run(
            command, input=f"{YES_LABEL}\n{NO_LABEL}".encode(), stdout=subprocess.PIPE
        )
        .stdout.decode("utf-8")
        .strip()
    )

    return result == YES_LABEL


def main(title: str = "Confirmations", question: str = "Are you sure?"):
    confirmed = confirm_cmd(title, question)

    if confirmed:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()
