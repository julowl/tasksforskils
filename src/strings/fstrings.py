"""
Exercises focused on f-strings: embedding expressions, formatting numbers, width and precision.
"""
from typing import Any


def format_price(name: str, price: float) -> str:
    """
    Return a string using an f-string that formats the item name and price with 2 decimal places.

    Example:
    >>> format_price("apple", 1.5)
    'apple: $1.50'
    """
    raise NotImplementedError


def padded_number(n: int, width: int) -> str:
    """
    Return the number `n` formatted with leading zeros to occupy `width` characters using an f-string.
    If width is less than the length of the number, return the number as-is.

    >>> padded_number(5, 3)
    '005'

    >>> padded_number(1234, 3)
    '1234'
    """
    raise NotImplementedError


def expression_inside(name: str, values: list[int]) -> str:
    """
    Use an f-string with an expression to return a summary string: "<name>: <sum(values)> items"

    >>> expression_inside("nums", [1,2,3])
    'nums: 6 items'
    """
    raise NotImplementedError


# -------------------- Tests --------------------
import unittest


class TestFormatPrice(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(format_price("apple", 1.5), "apple: $1.50")

    def test_rounding(self):
        self.assertEqual(format_price("x", 2.3456), "x: $2.35")

    def test_zero(self):
        self.assertEqual(format_price("free", 0.0), "free: $0.00")

    def test_negative(self):
        self.assertEqual(format_price("debt", -1.2), "debt: $-1.20")

    def test_large(self):
        self.assertEqual(format_price("big", 123456.789), "big: $123456.79")


class TestPaddedNumber(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(padded_number(5, 3), "005")

    def test_no_padding(self):
        self.assertEqual(padded_number(1234, 3), "1234")

    def test_zero_width(self):
        self.assertEqual(padded_number(7, 0), "7")

    def test_negative_number(self):
        self.assertEqual(padded_number(-3, 4), "-003")

    def test_large_width(self):
        self.assertEqual(padded_number(42, 6), "000042")


class TestExpressionInside(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(expression_inside("nums", [1, 2, 3]), "nums: 6 items")

    def test_empty(self):
        self.assertEqual(expression_inside("empty", []), "empty: 0 items")

    def test_negative(self):
        self.assertEqual(expression_inside("neg", [-1, -2]), "neg: -3 items")

    def test_single(self):
        self.assertEqual(expression_inside("one", [5]), "one: 5 items")

    def test_large(self):
        self.assertEqual(expression_inside("sum", list(range(10))), f"sum: {sum(range(10))} items")


if __name__ == "__main__":
    unittest.main()
