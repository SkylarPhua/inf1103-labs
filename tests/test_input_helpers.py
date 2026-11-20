import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from input_helpers import get_positive_float


class InputHelperTests(unittest.TestCase):
    def test_retries_until_price_is_positive(self) -> None:
        output = io.StringIO()

        with patch(
            "builtins.input",
            side_effect=["abc", "-5", "12.50"],
        ) as mock_input:
            with redirect_stdout(output):
                result = get_positive_float("Price: ")

        self.assertEqual(result, 12.5)
        self.assertEqual(mock_input.call_count, 3)
        self.assertEqual(
            output.getvalue().splitlines(),
            [
                "Please enter a valid number, e.g. 12.50",
                "Please enter a number greater than zero.",
            ],
        )


if __name__ == "__main__":
    unittest.main()