import unittest
from currencies import get_currencies


class TestGetCurrenciesSimplified(unittest.TestCase):

    def test_1_valid_usd(self):
        result = get_currencies(["USD"])
        self.assertIsNotNone(result)
        self.assertIn("USD", result)
        self.assertIsInstance(result["USD"], float)

    def test_2_invalid_url(self):
        with self.assertRaises(ConnectionError):
            get_currencies(["USD"], url="https://invalid-url")

    def test_3_missing_valute_key(self):
        with self.assertRaises(KeyError):
            get_currencies(["USD"], url="https://httpbin.org/json")

    def test_4_nonexistent_currency(self):
        with self.assertRaises(KeyError):
            get_currencies(["XYZ"])

    def test_5_multiple_currencies(self):
        result = get_currencies(["USD", "EUR"])
        self.assertIsNotNone(result)
        self.assertIn("USD", result)
        self.assertIn("EUR", result)


if __name__ == '__main__':
    unittest.main()
