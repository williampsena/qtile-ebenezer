class AppSettingsBarWidget:
    type: str
    args: dict
    def __init__(self, **kwargs) -> None: ...

class AppSettingsBar:
    position: str
    size: int
    margin: list[int]
    widgets: list[AppSettingsBarWidget]
    def __init__(self, **kwargs) -> None: ...
