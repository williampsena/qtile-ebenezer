from ebenezer.config.settings import load_settings_by_files as load_settings_by_files
from ebenezer.core.wallpaper import change_wallpaper as change_wallpaper

CHANGE_WALLPAPER_OPTION: str
CANCEL_OPTION: str

def get_base_dir(): ...
def rofi_menu(options, prompt, theme): ...
def main() -> None: ...
