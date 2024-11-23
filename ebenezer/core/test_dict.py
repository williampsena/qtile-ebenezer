import unittest

from ebenezer.core.dict import merge_dicts_recursive


class TestMergeDictsRecursive(unittest.TestCase):
    def test_merge_dicts_recursive(self):
        base = {"a": 1, "b": {"c": 2, "d": 3}, "e": 4}
        override = {"b": {"c": 20, "f": 6}, "g": 7}
        expected = {"a": 1, "b": {"c": 20, "d": 3, "f": 6}, "e": 4, "g": 7}
        result = merge_dicts_recursive(base, override)
        self.assertEqual(result, expected)

    def test_merge_with_empty_override(self):
        base = {"a": 1, "b": {"c": 2}}
        override = {}
        expected = {"a": 1, "b": {"c": 2}}
        result = merge_dicts_recursive(base, override)
        self.assertEqual(result, expected)

    def test_merge_with_empty_base(self):
        base = {}
        override = {"a": 1, "b": {"c": 2}}
        expected = {"a": 1, "b": {"c": 2}}
        result = merge_dicts_recursive(base, override)
        self.assertEqual(result, expected)

    def test_merge_with_non_dict_values(self):
        base = {"a": 1, "b": 2}
        override = {"b": {"c": 3}, "d": 4}
        expected = {"a": 1, "b": {"c": 3}, "d": 4}
        result = merge_dicts_recursive(base, override)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
