"""Recursion exercises: factorial, flattening nested lists, fibonacci.

Students implement classic recursive functions and handle base cases correctly.

Theory:
- Recursion: solve a problem by reducing it to smaller instances and defining a base case.
- Always ensure a terminating base case to prevent infinite recursion and stack overflow.
- For deep recursion consider iterative solutions; Python does not optimize tail calls.
"""
from typing import List, Any


def factorial(n: int) -> int:
    """Return n! for non-negative integer n using recursion.

    Requirements:
    - Raise ValueError for negative n.

    Examples:
    >>> factorial(0)
    1
    >>> factorial(4)
    24
    """
    raise NotImplementedError


def flatten(nested: List[Any]) -> List[Any]:
    """Flatten a nested list of arbitrary depth into a single list.

    Requirements:
    - Only lists should be flattened; other iterable-like objects are left as elements.

    Examples:
    >>> flatten([1, [2, [3, 4], 5], 6])
    [1, 2, 3, 4, 5, 6]
    """
    raise NotImplementedError


def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number (0-indexed) using recursion.

    Requirements:
    - fibonacci(0) == 0, fibonacci(1) == 1.
    - Raise ValueError for negative n.

    Examples:
    >>> fibonacci(5)
    5
    """
    raise NotImplementedError


# -------------------- Tests --------------------
import unittest


class TestFactorial(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_small(self):
        self.assertEqual(factorial(5), 120)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_medium(self):
        self.assertEqual(factorial(10), 3628800)


class TestFlatten(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(flatten([1, [2, 3], 4]), [1, 2, 3, 4])

    def test_deep(self):
        self.assertEqual(flatten([[[1], 2], 3]), [1, 2, 3])

    def test_empty(self):
        self.assertEqual(flatten([]), [])

    def test_mixed(self):
        self.assertEqual(flatten([1, [2, [3, [4]]], 5]), [1, 2, 3, 4, 5])

    def test_non_list_elements(self):
        self.assertEqual(flatten([1, (2, 3), [4]]), [1, (2, 3), 4])


class TestFibonacci(unittest.TestCase):
    def test_first(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_small(self):
        self.assertEqual(fibonacci(6), 8)

    def test_negative(self):
        with self.assertRaises(ValueError):
            fibonacci(-3)

    def test_medium(self):
        self.assertEqual(fibonacci(10), 55)

    def test_consistency(self):
        # check recursive identity
        self.assertEqual(fibonacci(7), fibonacci(6) + fibonacci(5))


if __name__ == '__main__':
    unittest.main()
