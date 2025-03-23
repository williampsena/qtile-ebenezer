from _typeshed import Incomplete
from ebenezer.config.settings import AppSettings as AppSettings, load_settings_by_files as load_settings_by_files
from ebenezer.core.notify import push_notification_no_history as push_notification_no_history
from ebenezer.core.requests import request_retry as request_retry
from ebenezer.core.theme import preload_colors as preload_colors

OUTPUT_FILE: str
QUOTE_OUTPUT_FILE: str
JOKE_CACHE_FILE: str
NO_JOKES: str
CACHE_FILE_LIMIT: Incomplete

def main(settings: AppSettings | None = None, startup: bool = False): ...
