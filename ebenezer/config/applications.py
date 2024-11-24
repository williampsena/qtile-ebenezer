"""
applications.py
---------------

This module provides a class to manage application settings.

Classes:
    AppSettingsApplications:
        Manages application settings including icons.
"""


class AppSettingsApplications:
    icons: dict[str, str] = {}

    def __init__(self, **kwargs):
        """
        Initializes the AppSettingsApplications with optional keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments to initialize the application settings.
        """
        self.icons = kwargs.get("icons", self.icons)
