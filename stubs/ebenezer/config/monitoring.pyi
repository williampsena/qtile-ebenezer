class AppSettingsMonitoring:
    default_color: str
    high_color: str
    medium_color: str
    threshold_medium: int
    threshold_high: int
    burn: bool
    def __init__(self, **kwargs) -> None: ...
