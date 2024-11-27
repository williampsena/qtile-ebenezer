"""
files.py
--------

This module provides functions to resolve file paths with variable substitution.

Functions:
    resolve_file_path(raw_path: str) -> str:
        Resolves a file path by substituting predefined variables.
"""

from pathlib import Path
from string import Template

home: str = str(Path.home())
qtile_home: str = str(Path.joinpath(Path(home), ".config/qtile"))
theme_home: str = str(Path.joinpath(Path(qtile_home), "themes"))

rofi_home: str = str(Path.joinpath(Path(qtile_home), "rofi"))
scripts = str(Path.joinpath(Path(qtile_home), "scripts"))


def resolve_file_path(raw_path: str, **kwargs: dict) -> str:
    """
    Resolves a file path by substituting predefined variables.

    Args:
        raw_path (str): The raw path template.

    Returns:
        str: The fully resolved and substituted path.
    """
    cmd_template = Template(raw_path)

    template_args = {
        "home": home,
        "qtile_home": qtile_home,
        "theme_home": theme_home,
        "rofi_home": rofi_home,
        "scripts": scripts,
        **kwargs,
    }
    return cmd_template.safe_substitute(template_args).strip()
