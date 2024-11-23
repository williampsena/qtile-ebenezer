"""
dict.py
-------

This module provides functions to merge dictionaries recursively.

Functions:
    merge_dicts_recursive(base: dict, override: dict) -> dict:
        Merges two dictionaries recursively.
"""


def merge_dicts_recursive(base: dict, override: dict) -> dict:
    """
    Merges two dictionaries recursively.

    Args:
        base (dict): The base dictionary.
        override (dict): The dictionary with overriding values.

    Returns:
        dict: The merged dictionary.
    """
    for key, value in override.items():
        if key in base and isinstance(base[key], dict) and isinstance(value, dict):
            merge_dicts_recursive(base[key], value)
        else:
            base[key] = value
    return base
