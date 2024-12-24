from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap


def read_yaml_file(filepath: str) -> CommentedMap:
    """
    Reads a YAML file and returns its contents as a CommentedMap.

    Args:
        filepath (str): The path to the YAML file.

    Returns:
        CommentedMap: The contents of the YAML file.
    """
    yaml = YAML()
    with open(filepath, "r", encoding="utf-8") as file:
        return yaml.load(file)


def write_yaml_file(filepath: str, data: CommentedMap) -> None:
    """
    Writes a CommentedMap to a YAML file.

    Args:
        filepath (str): The path to the YAML file.
        data (CommentedMap): The CommentedMap to write to the YAML file.
    """
    yaml = YAML()
    with open(filepath, "w", encoding="utf-8") as file:
        yaml.dump(data, file)


def update_yaml_property(filepath: str, property_path: str, value) -> None:
    """
    Updates a specific property in a YAML file while keeping other values intact.

    Args:
        filepath (str): The path to the YAML file.
        property_path (str): The dot-separated path to the property to update.
        value: The new value to set for the property.
    """
    data = read_yaml_file(filepath)
    keys = property_path.split(".")
    d = data
    for key in keys[:-1]:
        d = d.setdefault(key, CommentedMap())
    d[keys[-1]] = value
    write_yaml_file(filepath, data)
