"""
Exercises on parsing and searching strings: find, index, count, startswith, simple parsing tasks.
"""
from typing import Tuple, Optional


def find_substring(s: str, sub: str) -> int:
    """
    Return the first index of substring `sub` in `s`, or -1 if not found. Do not use str.find.

    >>> find_substring('hello', 'll')
    2

    >>> find_substring('a', 'b')
    -1
    """
    raise NotImplementedError


def split_key_value(line: str) -> Tuple[str, str]:
    """
    Split a string of the form 'key: value' into (key, value).
    Strip whitespace around key and value. If ':' is not present, raise ValueError.

    >>> split_key_value(' name : John ')
    ('name', 'John')
    """
    raise NotImplementedError


def extract_between(s: str, start: str, end: str) -> Optional[str]:
    """
    Return the substring found between the first occurrence of `start` and the next occurrence of `end` after it.
    If the markers are not found or in the wrong order return None.

    >>> extract_between('<a>content</a>', '<a>', '</a>')
    'content'
    """
    raise NotImplementedError


# -------------------- Tests --------------------
import unittest


class TestFindSubstring(unittest.TestCase):
    def test_found(self):
        self.assertEqual(find_substring('hello', 'll'), 2)

    def test_not_found(self):
        self.assertEqual(find_substring('abc', 'd'), -1)

    def test_at_start(self):
        self.assertEqual(find_substring('abc', 'a'), 0)

    def test_empty_sub(self):
        self.assertEqual(find_substring('abc', ''), 0)

    def test_overlap(self):
        self.assertEqual(find_substring('aaa', 'aa'), 0)


class TestSplitKeyValue(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(split_key_value(' name : John '), ('name', 'John'))

    def test_no_colon(self):
        with self.assertRaises(ValueError):
            split_key_value('no colon here')

    def test_multiple_colons(self):
        self.assertEqual(split_key_value('a: b: c'), ('a', 'b: c'))

    def test_empty_key_or_value(self):
        self.assertEqual(split_key_value(' : v '), ('', 'v'))
        self.assertEqual(split_key_value('k : '), ('k', ''))

    def test_strip(self):
        self.assertEqual(split_key_value('\tk\t: \tv\n'), ('k', 'v'))


class TestExtractBetween(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(extract_between('<a>content</a>', '<a>', '</a>'), 'content')

    def test_missing(self):
        self.assertIsNone(extract_between('hello', '<', '>'))

    def test_wrong_order(self):
        self.assertIsNone(extract_between('a[end]b', '[', '('))

    def test_multiple(self):
        self.assertEqual(extract_between('x<k>one</k><k>two</k>', '<k>', '</k>'), 'one')

    def test_empty_between(self):
        self.assertEqual(extract_between('a<>b', '<>', 'b'), '')


if __name__ == "__main__":
    unittest.main()
