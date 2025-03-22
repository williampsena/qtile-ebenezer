class AppSettingsKeyBinding:
    name: str
    keys: list[str]
    action: str
    command: str
    group: str
    def __init__(self, **kwargs) -> None: ...

def build_keybindings(items: list[dict]) -> list[AppSettingsKeyBinding]: ...
