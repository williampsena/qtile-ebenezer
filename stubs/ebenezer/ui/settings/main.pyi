import ttkbootstrap as ttk
from _typeshed import Incomplete
from ttkbootstrap.constants import *

from ebenezer.config.settings import load_settings_by_files as load_settings_by_files
from ebenezer.core.theme import apply_theme_color as apply_theme_color
from ebenezer.ui.settings.about_frame import AboutFrame as AboutFrame
from ebenezer.ui.settings.appearance_frame import AppearanceFrame as AppearanceFrame
from ebenezer.ui.settings.environment_frame import EnvironmentFrame as EnvironmentFrame
from ebenezer.ui.settings.styles import build_fonts as build_fonts
from ebenezer.ui.settings.styles import build_style as build_style
from ebenezer.ui.settings.wallpaper_frame import WallpaperFrame as WallpaperFrame

THEME_NAME: str

class EbenezerManager(ttk.Frame):
    theme_name: Incomplete
    fonts: Incomplete
    styles: Incomplete
    def __init__(self, master, theme_name: str) -> None: ...
    settings: Incomplete
    def load_settings(self) -> None: ...
    def build_ui(self) -> None: ...

def handle_sigint(signal_received, frame) -> None: ...
def main() -> None: ...
