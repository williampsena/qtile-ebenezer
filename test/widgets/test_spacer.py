import unittest

from libqtile import bar, widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.spacer import build_spacer_widget


class TestBuildSpacerWidget(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()

    def test_build_spacer_widget_default(self):
        kwargs = {}
        spacer_widget = build_spacer_widget(self.settings, kwargs)
        self.assertIsInstance(spacer_widget, widget.Spacer)
        self.assertEqual(spacer_widget.length_type, bar.STATIC)

    def test_build_spacer_widget_custom_args(self):
        kwargs = {"length": "calculated"}
        spacer_widget = build_spacer_widget(self.settings, kwargs)
        self.assertIsInstance(spacer_widget, widget.Spacer)
        self.assertEqual(spacer_widget.length_type, bar.CALCULATED)


if __name__ == "__main__":
    unittest.main()
