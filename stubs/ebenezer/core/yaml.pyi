from ruamel.yaml.comments import CommentedMap

def read_yaml_file(filepath: str) -> CommentedMap: ...
def write_yaml_file(filepath: str, data: CommentedMap) -> None: ...
def update_yaml_property(filepath: str, property_path: str, value) -> None: ...
