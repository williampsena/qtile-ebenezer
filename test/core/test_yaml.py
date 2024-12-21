import os
import tempfile
import unittest

from ruamel.yaml import YAML

from ebenezer.core.yaml import read_yaml_file, update_yaml_property, write_yaml_file


def _yaml_safe_load(file: str):
    yaml = YAML(typ="safe", pure=True)
    return yaml.load(file)


class TestYamlFunctions(unittest.TestCase):

    def test_read_yaml_file(self):
        with tempfile.NamedTemporaryFile(
            delete=False, mode="w", encoding="utf-8"
        ) as temp_file:
            temp_file.write("theme: old_theme\n")
            temp_file_path = temp_file.name

        try:
            expected_data = {"theme": "old_theme"}
            data = read_yaml_file(temp_file_path)
            self.assertEqual(data, expected_data)
        finally:
            os.remove(temp_file_path)

    def test_write_yaml_file(self):
        data = {"theme": "new_theme"}
        with tempfile.NamedTemporaryFile(
            delete=False, mode="w", encoding="utf-8"
        ) as temp_file:
            temp_file_path = temp_file.name

        try:
            write_yaml_file(temp_file_path, data)
            with open(temp_file_path, "r", encoding="utf-8") as file:
                written_data = _yaml_safe_load(file)
            self.assertEqual(written_data, data)
        finally:
            os.remove(temp_file_path)

    def test_update_yaml_property(self):
        with tempfile.NamedTemporaryFile(
            delete=False, mode="w", encoding="utf-8"
        ) as temp_file:
            temp_file.write("theme:\n  selected: old_theme\n  override: true\n")
            temp_file_path = temp_file.name

        try:
            property_path = "theme.selected"
            new_value = "new_theme"
            expected_data = {"theme": {"selected": "new_theme", "override": True}}

            update_yaml_property(temp_file_path, property_path, new_value)

            with open(temp_file_path, "r", encoding="utf-8") as file:
                updated_data = _yaml_safe_load(file)
            self.assertEqual(updated_data, expected_data)
        finally:
            os.remove(temp_file_path)


if __name__ == "__main__":
    unittest.main()
