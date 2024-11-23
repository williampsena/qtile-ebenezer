"""
yaml.py
-------

This module provides a function to read YAML files.

Functions:
    read_yaml_file(filepath: str) -> dict:
        Reads a YAML file and returns its contents as a dictionary.
"""

import yaml


def read_yaml_file(filepath: str) -> dict:
    """
    Reads a YAML file and returns its contents as a dictionary.

    Args:
        filepath (str): The path to the YAML file.

    Returns:
        dict: The contents of the YAML file.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)
