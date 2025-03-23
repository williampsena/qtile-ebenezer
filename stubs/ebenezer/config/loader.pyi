from _typeshed import Incomplete

from ebenezer.core.dict import merge_dicts_recursive as merge_dicts_recursive
from ebenezer.core.yaml import read_yaml_file as read_yaml_file

TEST_CONFIG: str
TEST_COLOR_CONFIG: str

def load_raw_test_settings(): ...
def load_raw_settings(
    config_filepath: Incomplete | None = None,
    colors_filepath: Incomplete | None = None,
    applications_filepath: Incomplete | None = None,
    keybindings_filepath: Incomplete | None = None,
) -> dict: ...
def merge_yaml(file_paths, merged_data: dict = {}) -> dict: ...
