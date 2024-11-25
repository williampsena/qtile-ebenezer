from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.core.notify import push_notification_no_history as push_notification_no_history
from ebenezer.core.requests import request_retry as request_retry

OUTPUT_FILE: str
QUOTE_OUTPUT_FILE: str

def lock_screen(settings: AppSettings): ...
def run_i3_lock(settings: AppSettings): ...
def build_lock_screen_widget(settings: AppSettings): ...
