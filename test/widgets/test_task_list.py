import unittest
from unittest.mock import MagicMock

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.task_list import (
    FontIconTaskList,
    _icon_replacement_parse_text,
    build_task_list_widget,
)


def _build_mock_window(name: str) -> MagicMock:
    window = MagicMock()
    window.name = name
    window.group.windows.index.return_value = 0
    window.get_wm_class.return_value = [name]

    return window


class TestFontIconTaskList(unittest.TestCase):

    def setUp(self):
        self.settings = AppSettings()
        self.settings.colors.fg_normal = "#FFFFFF"
        self.settings.colors.fg_blue = "#0000FF"
        self.settings.colors.bg_topbar_selected = "#FF0000"
        self.settings.fonts.font_icon = "FontAwesome"
        self.settings.fonts.font_icon_size = 12
        self.settings.applications.icons = {
            "firefox": "",
            "window": "",
        }

    def test_build_task_list_widget(self):
        kwargs = {}
        task_list_widget = build_task_list_widget(self.settings, kwargs)
        self.assertIsInstance(task_list_widget, FontIconTaskList)
        self.assertEqual(task_list_widget.font, "FontAwesome")
        self.assertEqual(task_list_widget.fontsize, 12)
        self.assertEqual(task_list_widget.foreground, "#FFFFFF")

    def test_get_taskname(self):
        task_list_widget = FontIconTaskList(
            parse_text=_icon_replacement_parse_text(self.settings),
        )

        task_list_widget.markup_normal = "{}"
        task_list_widget.markup_minimized = None
        task_list_widget.markup_maximized = None
        task_list_widget.markup_floating = None
        task_list_widget.markup_focused = None
        task_list_widget.markup_focused_floating = None
        task_list_widget.txt_minimized = "-"
        task_list_widget.txt_maximized = "+"
        task_list_widget.txt_floating = "~"
        task_list_widget.window_name_location = True
        task_list_widget.window_name_location_offset = 1

        icon_window = _build_mock_window("firefox")
        result = task_list_widget.get_taskname(icon_window)
        self.assertEqual(result, "-   [1] firefox")

        no_icon_window = _build_mock_window("browser")
        result = task_list_widget.get_taskname(no_icon_window)
        self.assertEqual(result, "-   [1] browser")


if __name__ == "__main__":
    unittest.main()
