import os
import tempfile
import unittest

from ebenezer.core.yaml import read_yaml_file


class TestReadYamlFile(unittest.TestCase):
    def test_read_yaml_file(self):
        with tempfile.NamedTemporaryFile(
            delete=False, mode="w", suffix=".yaml"
        ) as temp_file:
            temp_file.write(
                """
            key1: value1
            key2:
              subkey1: subvalue1
              subkey2: subvalue2
            """
            )
            temp_file_path = temp_file.name

        try:
            result = read_yaml_file(temp_file_path)

            expected_result = {
                "key1": "value1",
                "key2": {"subkey1": "subvalue1", "subkey2": "subvalue2"},
            }
            self.assertEqual(result, expected_result)
        finally:
            os.remove(temp_file_path)


if __name__ == "__main__":
    unittest.main()
