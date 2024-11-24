import unittest
from unittest.mock import MagicMock

from ebenezer.core.requests import request_retry


class TestRequestRetry(unittest.TestCase):
    def test_request_retry_success(self):
        operation = MagicMock(return_value="success")

        result = request_retry(operation, retries=3, delay=1)

        self.assertEqual(result, "success")
        operation.assert_called_once()

    def test_request_retry_failure(self):
        operation = MagicMock(side_effect=Exception("failure"))

        with self.assertRaises(Exception) as context:
            request_retry(operation, retries=3, delay=1)

        self.assertEqual(str(context.exception), "failure")
        self.assertEqual(operation.call_count, 3)

    def test_request_retry_partial_success(self):
        operation = MagicMock(
            side_effect=[Exception("failure"), Exception("failure"), "success"]
        )

        result = request_retry(operation, retries=3, delay=1)

        self.assertEqual(result, "success")
        self.assertEqual(operation.call_count, 3)


if __name__ == "__main__":
    unittest.main()
