import unittest

from ebenezer.widgets.formatter import burn_text


class TestBurnText(unittest.TestCase):
    def test_burn_text_left(self):
        text = "CPU"
        result = burn_text(text, position="left")
        self.assertEqual(result, "🔥 CPU")

    def test_burn_text_right(self):
        text = "CPU"
        result = burn_text(text, position="right")
        self.assertEqual(result, "CPU 🔥")

    def test_burn_text_default(self):
        text = "CPU"
        result = burn_text(text)
        self.assertEqual(result, "🔥 CPU")


if __name__ == "__main__":
    unittest.main()
