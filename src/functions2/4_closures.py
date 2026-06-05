"""Closures: creating functions that capture state from enclosing scopes.

Exercises include counters, simple validators, and a memoization closure.

Theory:
- Closures are functions that remember variables from their defining scope.
- Use nonlocal or mutable objects to maintain state across calls (e.g., counters).
- Closures are commonly used for encapsulation, factories, and lightweight memoization.
"""
from typing import Callable, Any, Dict


def make_counter(start: int = 0) -> Callable[[], int]:
    """Return a zero-argument function that increments and returns a counter.

    Requirements:
    - Each call to the returned function increments the internal counter by 1
      and returns the new value.

    Examples:
    >>> c = make_counter(10)
    >>> c()
    11
    >>> c()
    12
    """
    raise NotImplementedError


def password_checker(correct: str) -> Callable[[str], bool]:
    """Return a function that checks whether a provided password matches.

    Requirements:
    - The returned function accepts an input string and returns True if it
      equals the correct password, False otherwise.

    Examples:
    >>> check = password_checker('s3cret')
    >>> check('s3cret')
    True
    >>> check('wrong')
    False
    """
    raise NotImplementedError


def memoize_single_arg(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Return a memoized version of a single-argument function using a closure.

    Requirements:
    - Cache results by the single argument; repeated calls with the same
      argument must return cached result (do not call func again).

    Examples:
    >>> calls = {'n': 0}
    >>> def f(x):
    ...     calls['n'] += 1
    ...     return x * 2
    >>> mf = memoize_single_arg(f)
    >>> mf(2)
    4
    >>> mf(2)
    4
    >>> calls['n']
    1
    """
    raise NotImplementedError


# -------------------- Tests --------------------
import unittest


class TestMakeCounter(unittest.TestCase):
    def test_sequence(self):
        c = make_counter(0)
        self.assertEqual(c(), 1)
        self.assertEqual(c(), 2)
        self.assertEqual(c(), 3)

    def test_start(self):
        c = make_counter(10)
        self.assertEqual(c(), 11)

    def test_independent(self):
        a = make_counter(0)
        b = make_counter(100)
        self.assertEqual(a(), 1)
        self.assertEqual(b(), 101)
        self.assertEqual(a(), 2)

    def test_multiple_calls(self):
        c = make_counter(-1)
        for i in range(5):
            c()
        self.assertEqual(c(), 5)

    def test_type(self):
        c = make_counter(2)
        self.assertIsInstance(c(), int)


class TestPasswordChecker(unittest.TestCase):
    def test_correct(self):
        ck = password_checker('pw')
        self.assertTrue(ck('pw'))

    def test_incorrect(self):
        ck = password_checker('pw')
        self.assertFalse(ck('no'))

    def test_empty(self):
        ck = password_checker('')
        self.assertTrue(ck(''))
        self.assertFalse(ck(' '))

    def test_reuse(self):
        ck = password_checker('x')
        self.assertFalse(ck('y'))
        self.assertTrue(ck('x'))

    def test_type(self):
        ck = password_checker('1')
        self.assertFalse(ck(1))  # type: ignore


class TestMemoizeSingleArg(unittest.TestCase):
    def test_memoization(self):
        calls = {'n': 0}

        def f(x):
            calls['n'] += 1
            return x * x

        mf = memoize_single_arg(f)
        self.assertEqual(mf(3), 9)
        self.assertEqual(mf(3), 9)
        self.assertEqual(calls['n'], 1)

    def test_different_args(self):
        calls = {'n': 0}

        def f(x):
            calls['n'] += 1
            return x

        mf = memoize_single_arg(f)
        self.assertEqual(mf(1), 1)
        self.assertEqual(mf(2), 2)
        self.assertEqual(calls['n'], 2)

    def test_none_arg(self):
        def f(x):
            return 'ok'

        mf = memoize_single_arg(f)
        self.assertEqual(mf(None), 'ok')
        self.assertEqual(mf(None), 'ok')

    def test_unhashable_arg(self):
        # behaviour: unhashable args may raise TypeError when used as dict key; ensure it still works or raises
        def f(x):
            return len(x)

        mf = memoize_single_arg(f)
        try:
            mf([1, 2, 3])
            mf([1, 2, 3])
        except TypeError:
            # Acceptable if implementation requires hashable args
            self.assertTrue(True)

    def test_return_type(self):
        def f(x):
            return {'v': x}

        mf = memoize_single_arg(f)
        self.assertEqual(mf(5), {'v': 5})


if __name__ == '__main__':
    unittest.main()
