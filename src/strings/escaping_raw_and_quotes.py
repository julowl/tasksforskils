"""
Exercises on escaping characters, using raw strings, and working with single/double/triple quotes.
"""
from typing import Tuple


def make_quoted(s: str) -> str:
    """
    Return the string wrapped in double quotes. Any existing double quotes inside should be escaped with a backslash.

    >>> make_quoted('He said "Hi"')
    '"He said \\"Hi\\""'

    >>> make_quoted('simple')
    '"simple"'
    """
    raise NotImplementedError


def raw_path(path: str) -> str:
    """
    Return a raw-style representation for a Windows path: convert single backslashes into double backslashes
    so that it can be used in a string literal. Do not add surrounding quotes.

    >>> raw_path('C:\\Users\\me')
    'C:\\Users\\me'
    """
    raise NotImplementedError


def multiline_summary(lines: list[str]) -> Tuple[str, int]:
    """
    Join the provided lines into a single triple-quoted multiline string and return the tuple (joined_string, line_count).
    The joined string should have newline characters between lines, and should not have leading/trailing extra newlines.

    >>> multiline_summary(["a","b"])  # doctest: +ELLIPSIS
    ('a\n...b', 2)
    """
    raise NotImplementedError


# -------------------- Tests --------------------
import unittest


class TestMakeQuoted(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(make_quoted('simple'), '"simple"')

    def test_with_quotes(self):
        self.assertEqual(make_quoted('He said "Hi"'), '"He said \\"Hi\\""')

    def test_empty(self):
        self.assertEqual(make_quoted(''), '""')

    def test_only_quotes(self):
        self.assertEqual(make_quoted('""'), '"\\"\\""')

    def test_backslashes_unchanged(self):
        self.assertEqual(make_quoted('back\\slash'), '"back\\slash"')


class TestRawPath(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(raw_path('C:\\Users\\me'), 'C:\\Users\\me')

    def test_single_backslash(self):
        self.assertEqual(raw_path('a\\b'), 'a\\b')

    def test_multiple(self):
        self.assertEqual(raw_path('\\server\\share'), '\\server\\share')

    def test_no_backslash(self):
        self.assertEqual(raw_path('unix/path'), 'unix/path')

    def test_empty(self):
        self.assertEqual(raw_path(''), '')


class TestMultilineSummary(unittest.TestCase):
    def test_two_lines(self):
        joined, count = multiline_summary(["a", "b"])
        self.assertEqual(joined, "a\nb")
        self.assertEqual(count, 2)

    def test_empty_list(self):
        joined, count = multiline_summary([])
        self.assertEqual(joined, "")
        self.assertEqual(count, 0)

    def test_single_line(self):
        joined, count = multiline_summary(["only"])
        self.assertEqual(joined, "only")
        self.assertEqual(count, 1)

    def test_with_newlines_in_input(self):
        joined, count = multiline_summary(["a\n", "b"])
        self.assertEqual(joined, "a\n\nb")
        self.assertEqual(count, 2)

    def test_whitespace_lines(self):
        joined, count = multiline_summary([" ", "\t"])
        self.assertEqual(joined, " \n\t")
        self.assertEqual(count, 2)


if __name__ == "__main__":
    unittest.main()
