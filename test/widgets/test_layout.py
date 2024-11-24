import unittest

from ebenezer.widgets.layout import get_layout_icon


class TestGetLayoutIcon(unittest.TestCase):
    def test_get_layout_icon_known_layout(self):
        self.assertEqual(get_layout_icon("monadtall"), "󰕴")
        self.assertEqual(get_layout_icon("monadwide"), "󰜩")
        self.assertEqual(get_layout_icon("max"), "")
        self.assertEqual(get_layout_icon("stack"), "充")

    def test_get_layout_icon_unknown_layout(self):
        self.assertEqual(get_layout_icon("unknown"), "")


if __name__ == "__main__":
    unittest.main()
