"""
Basic string operations: length, slicing, concatenation, repetition.
This module contains simple exercises to practice core string manipulations.
"""
from typing import List


def count_vowels(s: str) -> int:
    """
    Count ASCII vowels in the given string (both lowercase and uppercase).

    >>> count_vowels("")
    0

    >>> count_vowels("Hello")
    2

    >>> count_vowels("AEIOU aeiou")
    10
    """
    raise NotImplementedError


def reverse_words(s: str) -> str:
    """
    Reverse the order of words in a string. Words are separated by whitespace.
    Preserve a single space between words in the result and strip leading/trailing whitespace.

    >>> reverse_words("  hello world  ")
    'world hello'

    >>> reverse_words("one two three")
    'three two one'
    """
    raise NotImplementedError


def repeat_and_truncate(s: str, n: int, max_len: int) -> str:
    """
    Repeat string `s` exactly `n` times and then truncate the result to at most `max_len` characters.
    If n <= 0 return an empty string. If max_len <= 0 return an empty string.

    >>> repeat_and_truncate("ab", 3, 5)
    'ababa'

    >>> repeat_and_truncate("x", 0, 10)
    ''
    """
    raise NotImplementedError


# -------------------- Tests --------------------
import unittest


class TestCountVowels(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(count_vowels(""), 0)

    def test_basic(self):
        self.assertEqual(count_vowels("Hello"), 2)

    def test_all_vowels(self):
        self.assertEqual(count_vowels("AEIOUaeiou"), 10)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("bcdfg"), 0)

    def test_mixed(self):
        self.assertEqual(count_vowels("Python is fun"), 4)


class TestReverseWords(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(reverse_words("one two"), "two one")

    def test_extra_spaces(self):
        self.assertEqual(reverse_words("  hello   world  "), "world hello")

    def test_single(self):
        self.assertEqual(reverse_words("single"), "single")

    def test_empty(self):
        self.assertEqual(reverse_words(""), "")

    def test_many_words(self):
        self.assertEqual(reverse_words("a b c d"), "d c b a")


class TestRepeatAndTruncate(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(repeat_and_truncate("ab", 3, 5), "ababa")

    def test_zero_n(self):
        self.assertEqual(repeat_and_truncate("x", 0, 5), "")

    def test_zero_max_len(self):
        self.assertEqual(repeat_and_truncate("x", 3, 0), "")

    def test_truncate_less(self):
        self.assertEqual(repeat_and_truncate("abc", 2, 4), "abca"[:4])

    def test_large(self):
        self.assertEqual(repeat_and_truncate("z", 100, 10), "z" * 10)


if __name__ == "__main__":
    unittest.main()
