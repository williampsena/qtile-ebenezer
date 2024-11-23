"""
command.py
----------

This module provides functions to build and run shell commands with optional timeout, and to create lazy commands for Qtile.

Functions:
    build_shell_command(raw_cmd: str, **kwargs: object) -> str:
        Builds a shell command by resolving file paths and substituting variables.

    run_shell_command(raw_cmd: str, timeout: Optional[float] = 10, **kwargs: object) -> subprocess.CompletedProcess:
        Runs a shell command with an optional timeout and returns the completed process.

    run_shell_command_stdout(raw_cmd: str, **kwargs: object) -> subprocess.CompletedProcess:
        Runs a shell command and captures the standard output.

    lazy_command(cmd: str | None, **kwargs: object):
        Creates a lazy command for Qtile that runs a shell command.

    lazy_spawn(cmd: str, **kwargs: object):
        Creates a lazy spawn command for Qtile that runs a shell command.
"""

import subprocess
from string import Template
from typing import Optional

from libqtile.lazy import lazy

from ebenezer.core.files import resolve_file_path

DEFAULT_TIMEOUT = 10


def build_shell_command(raw_cmd: str, **kwargs: object) -> str:
    """
    Builds a shell command by resolving file paths and substituting variables.

    Args:
        raw_cmd (str): The raw command template.
        **kwargs (object): Additional keyword arguments to substitute in the command template.

    Returns:
        str: The fully resolved and substituted command.
    """
    cmd_template = Template(resolve_file_path(raw_cmd))

    return cmd_template.safe_substitute(kwargs).strip()


def run_shell_command(
    raw_cmd: str, timeout: Optional[float] = 10, **kwargs: object
) -> subprocess.CompletedProcess:
    """
    Runs a shell command with an optional timeout and returns the completed process.

    Args:
        raw_cmd (str): The raw command template.
        timeout (Optional[float]): The timeout for the command execution. Defaults to 10 seconds.
        **kwargs (object): Additional keyword arguments to substitute in the command template.

    Returns:
        subprocess.CompletedProcess: The completed process after running the command.
    """

    if timeout:
        kwargs["timeout"] = timeout

    return subprocess.run(
        build_shell_command(raw_cmd, **kwargs),
        shell=True,
    )


def run_shell_command_stdout(
    raw_cmd: str, **kwargs: object
) -> subprocess.CompletedProcess:
    """
    Runs a shell command and captures the standard output.

    Args:
        raw_cmd (str): The raw command template.
        **kwargs (object): Additional keyword arguments to substitute in the command template.

    Returns:
        subprocess.CompletedProcess: The completed process after running the command with captured standard output.
    """
    return subprocess.run(
        build_shell_command(raw_cmd, **kwargs),
        shell=True,
        stdout=subprocess.PIPE,
        text=True,
    )


def lazy_command(cmd: str | None, **kwargs: object):
    """
    Creates a lazy command for Qtile that runs a shell command.

    Args:
        cmd (str | None): The shell command to run.
        **kwargs (object): Additional keyword arguments to substitute in the command template.

    Returns:
        function: A lazy function that runs the shell command.
    """

    @lazy.function
    def _inner(_qtile):
        if cmd is None:
            return

        return run_shell_command(build_shell_command(cmd, **kwargs))

    return _inner


def lazy_spawn(cmd: str, **kwargs: object):
    """
    Creates a lazy spawn command for Qtile that runs a shell command.

    Args:
        cmd (str): The shell command to run.
        **kwargs (object): Additional keyword arguments to substitute in the command template.

    Returns:
        function: A lazy function that spawns the shell command.
    """
    return lazy.spawn(build_shell_command(cmd, **kwargs))
