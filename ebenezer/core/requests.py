import time

import requests
from libqtile.log_utils import logger


def request_retry(operation, retries=5, delay=2) -> requests.Response:
    """
    Retries the given operation a specified number of times with a delay between attempts.

    Args:
        operation (callable): The operation to be retried.
        retries (int): The number of retry attempts. Defaults to 5.
        delay (int): The delay between attempts in seconds. Defaults to 2 seconds.

    Returns:
        Any: The result of the operation if successful.

    Raises:
        Exception: If all retry attempts fail.
    """
    for attempt in range(retries):
        try:
            return operation()
        except Exception as e:
            logger.warning(f"Attempt {attempt + 1} failed: {e}", exc_info=True)

            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise
