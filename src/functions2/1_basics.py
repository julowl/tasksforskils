"""Basic functions exercises.

Covers simple function implementation, string processing, and list splitting.

Theory:
- Functions encapsulate behavior: parameters, return values, and clear contracts.
- For palindromes normalize strings (lowercase, remove non-alphanumeric) before checking.
- List processing often preserves order; splitting returns multiple values (tuple).
"""
from typing import List, Tuple


def add(a: int, b: int) -> int:
    """Return the sum of two integers.

    Requirements:
    - Return the integer sum of a and b.

    Examples:
    >>> add(1, 2)
    3

    >>> add(-1, 1)
    0
    """
    summ = (a + b)
    return summ


def is_palindrome(s: str) -> bool:
    """Return True if the string s is a palindrome.

    Requirements:
    - Ignore case and non-alphanumeric characters (consider only letters and digits).

    Examples:
    >>> is_palindrome('A man, a plan, a canal: Panama')
    True

    >>> is_palindrome('hello')
    False
    """
    new_s = [_ for _ in s.lower() if _.isalpha()]
    left = 0
    right = len(new_s)-1
    while left <= right:
        if new_s[left] == new_s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True




def split_even_odd(nums: List[int]) -> Tuple[List[int], List[int]]:
    """Split a list of integers into (evens, odds) preserving order.

    Requirements:
    - Return a tuple of two lists: (even_numbers, odd_numbers).

    Examples:
    >>> split_even_odd([1,2,3,4])
    ([2, 4], [1, 3])

    >>> split_even_odd([])
    ([], [])
    """
    evens = []
    odds = []
    for i in nums:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    return evens, odds


# -------------------- Tests --------------------
import unittest


class TestAdd(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add(-5, -7), -12)

    def test_mixed(self):
        self.assertEqual(add(-1, 1), 0)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_large(self):
        self.assertEqual(add(10**6, 1), 1000001)


class TestIsPalindrome(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(is_palindrome('madam'))

    def test_phrase(self):
        self.assertTrue(is_palindrome('A man, a plan, a canal: Panama'))

    def test_false(self):
        self.assertFalse(is_palindrome('python'))

    def test_empty(self):
        self.assertTrue(is_palindrome(''))

    def test_numbers(self):
        self.assertTrue(is_palindrome('1221'))


class TestSplitEvenOdd(unittest.TestCase):
    def test_mixed(self):
        ev, od = split_even_odd([1, 2, 3, 4, 5])
        self.assertEqual(ev, [2, 4])
        self.assertEqual(od, [1, 3, 5])

    def test_empty(self):
        ev, od = split_even_odd([])
        self.assertEqual(ev, [])
        self.assertEqual(od, [])

    def test_all_even(self):
        ev, od = split_even_odd([2, 4, 6])
        self.assertEqual(ev, [2, 4, 6])
        self.assertEqual(od, [])

    def test_all_odd(self):
        ev, od = split_even_odd([1, 3, 5])
        self.assertEqual(ev, [])
        self.assertEqual(od, [1, 3, 5])

    def test_order_preserved(self):
        ev, od = split_even_odd([2, 1, 4, 3])
        self.assertEqual(ev, [2, 4])
        self.assertEqual(od, [1, 3])


if __name__ == '__main__':
    unittest.main()
