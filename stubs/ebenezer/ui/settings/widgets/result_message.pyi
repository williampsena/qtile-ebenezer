from typing import Any

import ttkbootstrap as ttk
from _typeshed import Incomplete

from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.ui.settings.styles import build_fonts as build_fonts

class ResultMessageWidget(ttk.Label):
    settings: Incomplete
    fonts: Incomplete
    def __init__(self, settings: AppSettings, master: Any, **kwargs) -> None: ...
    def reset(self) -> None: ...
    def set_message(self, kind: str, message: str): ...
