from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from _typeshed import Incomplete
from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.ui.settings.styles import build_fonts as build_fonts
from ebenezer.ui.settings.widgets.label import build_label as build_label

class AboutFrame(ttk.Frame):
    settings: AppSettings
    DESCRIPTION: str
    QUOTE: str
    app: Incomplete
    fonts: Incomplete
    def __init__(self, settings: AppSettings, app: ttk.Window, parent) -> None: ...
