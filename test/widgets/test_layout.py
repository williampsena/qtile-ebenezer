import unittest

from ebenezer.widgets.layout import get_layout_icon


class TestGetLayoutIcon(unittest.TestCase):
    def test_get_layout_icon_known_layout(self):
        self.assertEqual(get_layout_icon("bsp"), "")
        self.assertEqual(get_layout_icon("columns"), "")
        self.assertEqual(get_layout_icon("floating"), "")
        self.assertEqual(get_layout_icon("matrix"), "󰘨")
        self.assertEqual(get_layout_icon("max"), "")
        self.assertEqual(get_layout_icon("monadtall"), "󰕴")
        self.assertEqual(get_layout_icon("monadthreecol"), "")
        self.assertEqual(get_layout_icon("monadwide"), "󰜩")
        self.assertEqual(get_layout_icon("plasma"), "")
        self.assertEqual(get_layout_icon("ratiotile"), "")
        self.assertEqual(get_layout_icon("screensplit"), "")
        self.assertEqual(get_layout_icon("slice"), "")
        self.assertEqual(get_layout_icon("spiral"), "")
        self.assertEqual(get_layout_icon("stack"), "")
        self.assertEqual(get_layout_icon("tile"), "")
        self.assertEqual(get_layout_icon("treetab"), "")
        self.assertEqual(get_layout_icon("verticaltile"), "")
        self.assertEqual(get_layout_icon("zoomy"), "")

    def test_get_layout_icon_unknown_layout(self):
        self.assertEqual(get_layout_icon("unknown"), "")


if __name__ == "__main__":
    unittest.main()
