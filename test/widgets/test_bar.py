import unittest

from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.bar import _build_separator


class TestBuildSeparator(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()

    def test_build_separator_default(self):
        args = {}
        separator_widget = _build_separator(self.settings, args)
        self.assertIsInstance(separator_widget, widget.Sep)

    def test_build_separator_custom_args(self):
        args = {"linewidth": 2, "foreground": "#000000"}
        separator_widget = _build_separator(self.settings, args)
        self.assertIsInstance(separator_widget, widget.Sep)
        self.assertEqual(separator_widget.linewidth, 2)
        self.assertEqual(separator_widget.foreground, "#000000")


if __name__ == "__main__":
    unittest.main()
