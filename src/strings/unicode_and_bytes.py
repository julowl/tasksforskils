"""
Exercises on Unicode, ord/chr, normalization basics, and encoding/decoding to bytes.
"""
from typing import Tuple
import unicodedata


def codepoints(s: str) -> list[int]:
    """
    Return a list of Unicode codepoints (integers) for each character in the string.

    >>> codepoints('A')
    [65]

    >>> codepoints('€')  # euro sign
    [8364]
    """
    raise NotImplementedError


def to_utf8_bytes(s: str) -> bytes:
    """
    Encode the given string to UTF-8 bytes and return them.

    >>> to_utf8_bytes('hi')
    b'hi'
    """
    raise NotImplementedError


def normalize_nfc(s: str) -> Tuple[str, bool]:
    """
    Normalize the string to NFC form and return a tuple (normalized_string, changed)
    where changed is True if the normalization changed the content.

    >>> normalize_nfc('e\u0301')[1]  # e + combining acute
    True
    """
    raise NotImplementedError


# -------------------- Tests --------------------
import unittest


class TestCodepoints(unittest.TestCase):
    def test_ascii(self):
        self.assertEqual(codepoints('ABC'), [65, 66, 67])

    def test_euro(self):
        self.assertEqual(codepoints('€'), [8364])

    def test_empty(self):
        self.assertEqual(codepoints(''), [])

    def test_emoji(self):
        # emoji is a single codepoint in many cases
        res = codepoints('🙂')
        self.assertTrue(all(isinstance(x, int) for x in res))

    def test_multichar(self):
        self.assertEqual(codepoints('a£b'), [97, 163, 98])


class TestToUtf8Bytes(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(to_utf8_bytes('hi'), b'hi')

    def test_unicode(self):
        self.assertEqual(to_utf8_bytes('€'), '€'.encode('utf-8'))

    def test_empty(self):
        self.assertEqual(to_utf8_bytes(''), b'')

    def test_emoji(self):
        self.assertEqual(to_utf8_bytes('🙂'), '🙂'.encode('utf-8'))

    def test_long(self):
        s = 'a' * 100
        self.assertEqual(to_utf8_bytes(s), b'a' * 100)


class TestNormalizeNFC(unittest.TestCase):
    def test_combining(self):
        norm, changed = normalize_nfc('e\u0301')
        self.assertTrue(changed)
        self.assertEqual(norm, 'é')

    def test_already(self):
        norm, changed = normalize_nfc('é')
        self.assertFalse(changed)
        self.assertEqual(norm, 'é')

    def test_empty(self):
        norm, changed = normalize_nfc('')
        self.assertFalse(changed)
        self.assertEqual(norm, '')

    def test_multiple(self):
        s = 'A\u030A'  # A + ring
        norm, changed = normalize_nfc(s)
        self.assertTrue(changed)

    def test_idempotent(self):
        s = 'cafe\u0301'
        norm1, _ = normalize_nfc(s)
        norm2, _ = normalize_nfc(norm1)
        self.assertEqual(norm1, norm2)


if __name__ == "__main__":
    unittest.main()
