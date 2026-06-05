"""Lambdas, map, filter, and sorting with key functions.

Exercises focus on small anonymous functions and using functional utilities.

Theory:
- lambda creates small anonymous functions: lambda x: x+1.
- map and filter return iterators in Python 3; convert to list() to realize results.
- sorted accepts a key function to compute comparison keys; use key for custom ordering.
"""
from typing import Callable, Iterable, List, Any


def apply_map(nums: Iterable[int], func: Callable[[int], int]) -> List[int]:
    """Apply func to each element of nums and return a list of results.

    Examples:
    >>> apply_map([1,2,3], lambda x: x+1)
    [2, 3, 4]
    """
    raise NotImplementedError


def filter_and_square(nums: Iterable[int]) -> List[int]:
    """Return squares of positive integers from nums using filter/map semantics.

    Requirements:
    - Keep only items > 0, then square them, and return as list preserving order.

    Examples:
    >>> filter_and_square([-1, 0, 2, 3])
    [4, 9]
    """
    raise NotImplementedError


def sort_by_key(items: Iterable[Any], key_func: Callable[[Any], Any]) -> List[Any]:
    """Return a list of items sorted by key_func(item).

    Examples:
    >>> sort_by_key(['aa', 'b', 'ccc'], key_func=len)
    ['b', 'aa', 'ccc']
    """
    raise NotImplementedError


# -------------------- Tests --------------------
import unittest


class TestApplyMap(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(apply_map([1, 2, 3], lambda x: x + 1), [2, 3, 4])

    def test_empty(self):
        self.assertEqual(apply_map([], lambda x: x * 2), [])

    def test_negative(self):
        self.assertEqual(apply_map([-1, -2], abs), [1, 2])

    def test_identity(self):
        self.assertEqual(apply_map([1, 2], lambda x: x), [1, 2])

    def test_large(self):
        self.assertEqual(apply_map([1000], lambda x: x + 1), [1001])


class TestFilterAndSquare(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(filter_and_square([-1, 0, 2, 3]), [4, 9])

    def test_all_negative(self):
        self.assertEqual(filter_and_square([-3, -2]), [])

    def test_zero_and_positive(self):
        self.assertEqual(filter_and_square([0, 1]), [1])

    def test_order(self):
        self.assertEqual(filter_and_square([3, 1, 2]), [9, 1, 4])

    def test_single(self):
        self.assertEqual(filter_and_square([5]), [25])


class TestSortByKey(unittest.TestCase):
    def test_len(self):
        self.assertEqual(sort_by_key(['aa', 'b', 'ccc'], key_func=len), ['b', 'aa', 'ccc'])

    def test_numeric_key(self):
        self.assertEqual(sort_by_key([1, 2, 3], key_func=lambda x: -x), [3, 2, 1])

    def test_tuples(self):
        items = [(1, 'b'), (2, 'a'), (1, 'a')]
        self.assertEqual(sort_by_key(items, key_func=lambda x: (x[0], x[1])), [(1, 'a'), (1, 'b'), (2, 'a')])

    def test_empty(self):
        self.assertEqual(sort_by_key([], key_func=lambda x: x), [])

    def test_preserve_items(self):
        data = ['x', 'yyy', 'zz']
        self.assertEqual(sort_by_key(data, key_func=len), ['x', 'zz', 'yyy'])


if __name__ == '__main__':
    unittest.main()
