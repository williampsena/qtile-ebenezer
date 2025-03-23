"""
This module defines classes for managing scratchpad dropdown settings in a Qtile configuration.

Classes:
    AppSettingsScratchpadsDropdown: Represents the settings for a single scratchpad dropdown.
    AppSettingsScratchpads: Manages a collection of scratchpad dropdowns.
"""


class AppSettingsScratchpadsDropdown:
    """
    Represents the settings for a single scratchpad dropdown.
    """

    name: str = ""
    command: str = ""
    args: dict[str, any] = {}

    def __init__(self, **kwargs):
        """
        Initializes the AppSettingsScratchpadsDropdown with optional keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments to initialize the scratchpad dropdown settings.
            - command (str): The command to execute for the scratchpad dropdown.
            - args (dict[str, any]): Additional arguments for the scratchpad dropdown.
        """
        self.name = kwargs.get("name", self.name)
        self.command = kwargs.get("command", self.command)
        self.args = kwargs.get("args", self.args)


class AppSettingsScratchpads:
    """
    Manages a collection of scratchpad dropdowns.
    """

    dropdowns: dict[str, AppSettingsScratchpadsDropdown] = {}

    def __init__(self, **kwargs):
        """
        Initializes an instance of the AppSettingsScratchpads class.

        This constructor allows for the initialization of the scratchpad dropdown settings
        using optional keyword arguments.
            **kwargs: Arbitrary keyword arguments for initialization.
                - dropdowns (dict[str, AppSettingsScratchpadsDropdown], optional):
                  A dictionary mapping string keys to AppSettingsScratchpadsDropdown objects.
                  If not provided, the existing value of `self.dropdowns` is used.

        """
        dropdowns = kwargs.get("dropdowns", {})

        if dropdowns:
            self.dropdowns = _build_dropdown(dropdowns)


def _build_dropdown(args: dict[str, any]) -> dict[str, AppSettingsScratchpadsDropdown]:
    return {
        key: AppSettingsScratchpadsDropdown(**{"name": key} | value)
        for key, value in args.items()
    }
