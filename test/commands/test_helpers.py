import unittest

from ebenezer.commands.volume import run_command


class TestHelpers(unittest.TestCase):
    def test_run_command(self):
        result = run_command("echo 50%")
        self.assertEqual(result, "50%")


if __name__ == "__main__":
    unittest.main()
