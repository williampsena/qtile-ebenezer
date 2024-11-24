import unittest

from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.arrow import build_arrow_widget


class TestBuildArrowWidget(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()
        self.settings.fonts.font_arrow = "FontAwesome"
        self.settings.fonts.font_arrow_size = 12
        self.settings.colors.bg_topbar_arrow = "#FFFFFF"

    def test_build_arrow_widget_default(self):
        kwargs = {}
        arrow_widget = build_arrow_widget(self.settings, kwargs)
        self.assertIsInstance(arrow_widget, widget.TextBox)
        self.assertEqual(arrow_widget.text, "")
        self.assertEqual(arrow_widget.font, "FontAwesome")
        self.assertEqual(arrow_widget.fontsize, 12)
        self.assertEqual(arrow_widget.foreground, "#FFFFFF")
        self.assertEqual(arrow_widget.padding, 0)

    def test_build_arrow_widget_custom_text(self):
        kwargs = {"text": ""}
        arrow_widget = build_arrow_widget(self.settings, kwargs)
        self.assertIsInstance(arrow_widget, widget.TextBox)
        self.assertEqual(arrow_widget.text, "")

    def test_build_arrow_widget_custom_args(self):
        kwargs = {"fontsize": 14, "foreground": "#000000"}
        arrow_widget = build_arrow_widget(self.settings, kwargs)
        self.assertIsInstance(arrow_widget, widget.TextBox)
        self.assertEqual(arrow_widget.fontsize, 14)
        self.assertEqual(arrow_widget.foreground, "#000000")


if __name__ == "__main__":
    unittest.main()
