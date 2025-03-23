import ttkbootstrap as ttk
from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.ui.settings.styles import FontStyles as FontStyles

def build_label(parent_frame: ttk.Frame, app: ttk.Window, settings: AppSettings, text: str, font: FontStyles = None, link: str = None, cursor: str = None, text_color: str = None, bootstyle: str = None, justify: str = None) -> ttk.Label: ...
