import unittest
import io
from logger import logger


class TestLoggerSimplified(unittest.TestCase):

    def test_1_success(self):
        stream = io.StringIO()

        @logger(handle=stream)
        def add(a, b):
            return a + b

        result = add(2, 3)
        self.assertEqual(result, 5)
        logs = stream.getvalue()
        self.assertIn("Start add", logs)
        self.assertIn("Success add", logs)

    def test_2_error(self):
        stream = io.StringIO()

        @logger(handle=stream)
        def div(a, b):
            return a / b

        with self.assertRaises(ZeroDivisionError):
            div(1, 0)
        logs = stream.getvalue()
        self.assertIn("ERROR", logs)
        self.assertIn("ZeroDivisionError", logs)


if __name__ == '__main__':
    unittest.main()
