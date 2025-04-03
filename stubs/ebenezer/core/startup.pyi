from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.core.command import run_shell_command as run_shell_command

DEFAULT_TIMEOUT: int

def run_startup_once(settings: AppSettings): ...
