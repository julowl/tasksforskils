"""
Advanced string manipulations: split/join, translate, maketrans, templates and more.
"""
from typing import Dict, List


def translate_vowels(s: str, mapping: Dict[str, str]) -> str:
    """
    Replace characters in `s` according to `mapping` dict using str.translate semantics.
    mapping maps single-character strings to replacement strings.

    Example:
    >>> translate_vowels('hello', {'e':'3','o':'0'})
    'h3ll0'
    """
    raise NotImplementedError


def smart_split(s: str) -> List[str]:
    """
    Split string `s` into words using whitespace; ignore extra whitespace and return list of words.

    >>> smart_split('  a   b c ')
    ['a','b','c']
    """
    raise NotImplementedError


def join_lines(lines: List[str]) -> str:
    """
    Join a list of lines into a single string with '\n' between lines.
    Ensure there's no trailing newline at the end.

    >>> join_lines(['a','b'])
    'a\nb'
    """
    raise NotImplementedError


# -------------------- Tests --------------------
import unittest


class TestTranslateVowels(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(translate_vowels('hello', {'e': '3', 'o': '0'}), 'h3ll0')

    def test_no_change(self):
        self.assertEqual(translate_vowels('abc', {}), 'abc')

    def test_upper_lower(self):
        self.assertEqual(translate_vowels('Ae', {'A': '4', 'e': '3'}), '43')

    def test_full_mapping(self):
        s = 'aeiou'
        m = {c: str(i) for i, c in enumerate('aeiou')}
        self.assertEqual(translate_vowels(s, m), '01234')

    def test_nonexistent_chars(self):
        self.assertEqual(translate_vowels('xyz', {'a':'1'}), 'xyz')


class TestSmartSplit(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(smart_split('  a   b c '), ['a', 'b', 'c'])

    def test_empty(self):
        self.assertEqual(smart_split('   '), [])

    def test_tabs_newlines(self):
        self.assertEqual(smart_split('\ta\n b\t'), ['a', 'b'])

    def test_single(self):
        self.assertEqual(smart_split('word'), ['word'])

    def test_multiple_spaces(self):
        self.assertEqual(smart_split('a    b'), ['a', 'b'])


class TestJoinLines(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(join_lines(['a', 'b']), 'a\nb')

    def test_single(self):
        self.assertEqual(join_lines(['only']), 'only')

    def test_empty(self):
        self.assertEqual(join_lines([]), '')

    def test_trailing_newlines_in_input(self):
        self.assertEqual(join_lines(['a\n', 'b']), 'a\n\nb')

    def test_many(self):
        self.assertEqual(join_lines(['1', '2', '3']), '1\n2\n3')


if __name__ == "__main__":
    unittest.main()
