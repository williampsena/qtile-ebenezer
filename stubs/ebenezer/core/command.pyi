import subprocess

from ebenezer.core.files import resolve_file_path as resolve_file_path

DEFAULT_TIMEOUT: int

def build_shell_command(raw_cmd: str, **kwargs: object) -> str: ...
def run_shell_command(
    raw_cmd: str, timeout: float | None = 10, **kwargs: object
) -> subprocess.CompletedProcess: ...
def run_shell_command_stdout(
    raw_cmd: str, **kwargs: object
) -> subprocess.CompletedProcess: ...
def lazy_command(cmd: str | None, **kwargs: object): ...
def lazy_spawn(cmd: str, **kwargs: object): ...
