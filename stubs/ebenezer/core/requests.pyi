import requests

def request_retry(operation, retries: int = 5, delay: int = 2) -> requests.Response: ...
