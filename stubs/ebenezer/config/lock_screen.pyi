class AppSettingsLockScreen:
    command: str
    timeout: int
    font: str
    font_size: int
    quote_font_path: str
    quote_font_size: int
    joke_providers: str
    quote_foreground_color: str
    quote_text_color: str
    icanhazdad_joke_url: str
    reddit_joke_url: str
    blurtype: str
    def __init__(self, **kwargs) -> None: ...
