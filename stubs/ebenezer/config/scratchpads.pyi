class AppSettingsScratchpadsDropdown:
    name: str
    command: str
    args: dict[str, any]
    def __init__(self, **kwargs) -> None: ...

class AppSettingsScratchpads:
    dropdowns: dict[str, AppSettingsScratchpadsDropdown]
    def __init__(self, **kwargs) -> None: ...
