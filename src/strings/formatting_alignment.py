"""
Exercises on advanced formatting: str.format, alignment, padding, and numeric formats.
"""
from typing import Iterable


def align_text(s: str, width: int, align: str = "<") -> str:
    """
    Align text `s` into a field of `width` characters.
    align can be '<' (left), '>' (right), or '^' (center).
    If width is less than or equal to len(s), return s unchanged.

    >>> align_text('hi', 5, '<')
    'hi   '

    >>> align_text('hi', 5, '>')
    '   hi'
    """
    raise NotImplementedError


def format_percent(value: float) -> str:
    """
    Format a floating value as a percentage with one decimal place using format specification.
    Example: 0.1234 -> '12.3%'

    >>> format_percent(0.125)
    '12.5%'
    """
    raise NotImplementedError


def join_with_separator(items: Iterable[str], sep: str = ", ") -> str:
    """
    Join the provided iterable of strings using the given separator. Empty iterable -> empty string.

    >>> join_with_separator(['a','b','c'], '-')
    'a-b-c'
    """
    raise NotImplementedError


# -------------------- Tests --------------------
import unittest


class TestAlignText(unittest.TestCase):
    def test_left(self):
        self.assertEqual(align_text('hi', 5, '<'), 'hi   ')

    def test_right(self):
        self.assertEqual(align_text('hi', 5, '>'), '   hi')

    def test_center(self):
        self.assertEqual(align_text('hi', 5, '^'), ' hi  ')

    def test_no_change(self):
        self.assertEqual(align_text('hello', 3, '<'), 'hello')

    def test_invalid_align(self):
        # default to left alignment on invalid align
        self.assertEqual(align_text('x', 3, '?'), 'x  ')


class TestFormatPercent(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(format_percent(0.125), '12.5%')

    def test_zero(self):
        self.assertEqual(format_percent(0.0), '0.0%')

    def test_one(self):
        self.assertEqual(format_percent(1.0), '100.0%')

    def test_small(self):
        self.assertEqual(format_percent(0.00123), '0.1%')

    def test_rounding(self):
        self.assertEqual(format_percent(0.9995), '99.9%')


class TestJoinWithSeparator(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(join_with_separator(['a','b','c'], '-'), 'a-b-c')

    def test_empty(self):
        self.assertEqual(join_with_separator([], ','), '')

    def test_single(self):
        self.assertEqual(join_with_separator(['only'], ','), 'only')

    def test_default_sep(self):
        self.assertEqual(join_with_separator(['x','y']), 'x, y')

    def test_generator(self):
        self.assertEqual(join_with_separator((str(i) for i in range(3)), '|'), '0|1|2')


if __name__ == "__main__":
    unittest.main()
