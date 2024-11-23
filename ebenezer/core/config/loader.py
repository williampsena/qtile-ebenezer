"""
loader.py
---------

This module provides functions to load and merge YAML configuration files.

Functions:
    load_raw_test_settings() -> dict:
        Loads raw test settings from predefined test configuration files.

    load_raw_settings(config_filepath=None, colors_filepath=None, applications_filepath=None, keybindings_filepath=None) -> dict:
        Loads raw settings from the specified configuration files.

    merge_yaml(file_paths, merged_data: dict = {}) -> dict:
        Merges multiple YAML files into a single dictionary.
"""

from ebenezer.core.dict import merge_dicts_recursive
from ebenezer.core.yaml import read_yaml_file

TEST_CONFIG = "config.test.yml"
TEST_COLOR_CONFIG = "colors.test.yml"


def load_raw_test_settings():
    """
    Loads raw test settings from predefined test configuration files.

    Returns:
        dict: The merged raw test settings.
    """
    return load_raw_settings(
        config_filepath=TEST_CONFIG, colors_filepath=TEST_COLOR_CONFIG
    )


def load_raw_settings(
    config_filepath=None,
    colors_filepath=None,
    applications_filepath=None,
    keybindings_filepath=None,
) -> dict:
    """
    Loads raw settings from the specified configuration files.

    Args:
        config_filepath (str, optional): The path to the config file. Defaults to None.
        colors_filepath (str, optional): The path to the colors file. Defaults to None.
        applications_filepath (str, optional): The path to the applications file. Defaults to None.
        keybindings_filepath (str, optional): The path to the keybindings file. Defaults to None.

    Returns:
        dict: The merged raw settings.
    """
    return merge_yaml(
        [colors_filepath, applications_filepath, keybindings_filepath, config_filepath]
    )


def merge_yaml(file_paths, merged_data: dict = {}) -> dict:
    """
    Merges multiple YAML files into a single dictionary.

    Args:
        file_paths (list): A list of file paths to the YAML files.
        merged_data (dict, optional): The initial merged data. Defaults to {}.

    Returns:
        dict: The merged data from all the YAML files.
    """
    for file_path in file_paths:
        if file_path:
            data = read_yaml_file(file_path)
            merged_data = merge_dicts_recursive(merged_data, data)

    return merged_data
