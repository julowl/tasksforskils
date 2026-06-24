"""Exercises on decorators: adding behavior to functions.

Students will implement decorators that validate inputs, count calls, and check return types.

Theory:
- Decorators wrap functions to add behavior before/after the call (validation, logging, caching).
- Use functools.wraps to preserve original function metadata when writing wrappers.
- Decorators can be parameterized (factories) to accept configuration like expected types.
"""
from typing import Callable, Any, Type


def ensure_non_negative(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator: raise ValueError if any positional numeric argument is negative.

    Requirements:
    - Before calling func, inspect positional args; if any arg is int or float and
      is negative, raise ValueError. Otherwise call func and return its result.

    Examples:
    >>> @ensure_non_negative
    ... def f(x):
    ...     return x
    >>> f(1)
    1
    """



    def wrapper(*args):

        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
              raise ValueError("arg can't be negative")

        return func(*args)

    return wrapper


def count_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator: add a call_count attribute to the function object that tracks
    how many times the function was called.

    Requirements:
    - The returned wrapper must have an integer attribute call_count that
      increments each time the function is called.

    Examples:
    >>> @count_calls
    ... def f():
    ...     return None
    >>> f()
    >>> f.call_count
    1
    """
    def calls(*args):
        calls.call_count += 1
        return func(*args)

    calls.call_count = 0

    return calls


def ensure_return_type(expected: Type) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator factory: ensure the wrapped function returns an instance of expected.

    Requirements:
    - If the wrapped function returns a value not isinstance(value, expected),
      raise TypeError.

    Examples:
    >>> @ensure_return_type(int)
    ... def f():
    ...     return 1
    >>> f()
    1
    """

    def decorator(func):
        def types(*args):
            value = func(*args)
            if not isinstance(value, expected):
                raise TypeError
            return value

        return types
    return decorator


# -------------------- Tests --------------------
import unittest


class TestEnsureNonNegative(unittest.TestCase):
    def test_positive(self):
        @ensure_non_negative
        def f(x):
            return x
        self.assertEqual(f(5), 5)

    def test_zero(self):
        @ensure_non_negative
        def f(x):
            return x
        self.assertEqual(f(0), 0)

    def test_negative_raises(self):
        @ensure_non_negative
        def f(x):
            return x
        with self.assertRaises(ValueError):
            f(-1)

    def test_non_numeric_ok(self):
        @ensure_non_negative
        def f(x):
            return x
        self.assertEqual(f('a'), 'a')

    def test_multiple_args(self):
        @ensure_non_negative
        def f(x, y):
            return x + (y if isinstance(y, int) else 0)
        with self.assertRaises(ValueError):
            f(1, -2)


class TestCountCalls(unittest.TestCase):
    def test_basic(self):
        @count_calls
        def f():
            return 1
        self.assertEqual(getattr(f, 'call_count', 0), 0)
        f()
        self.assertEqual(f.call_count, 1)
        f()
        self.assertEqual(f.call_count, 2)

    def test_multiple_functions(self):
        @count_calls
        def a():
            return 1

        @count_calls
        def b():
            return 2

        a()
        a()
        b()
        self.assertEqual(a.call_count, 2)
        self.assertEqual(b.call_count, 1)

    def test_with_args(self):
        @count_calls
        def f(x):
            return x
        f(3)
        self.assertEqual(f.call_count, 1)

    def test_return_value_preserved(self):
        @count_calls
        def f(x):
            return x * 2
        self.assertEqual(f(4), 8)
        self.assertEqual(f.call_count, 1)

    def test_attribute_exists(self):
        @count_calls
        def f():
            pass
        self.assertTrue(hasattr(f, 'call_count'))


class TestEnsureReturnType(unittest.TestCase):
    def test_correct(self):
        @ensure_return_type(int)
        def f():
            return 3
        self.assertEqual(f(), 3)

    def test_incorrect(self):
        @ensure_return_type(str)
        def f():
            return 1
        with self.assertRaises(TypeError):
            f()

    def test_with_args(self):
        @ensure_return_type(int)
        def f(x):
            return x
        self.assertEqual(f(5), 5)

    def test_none(self):
        @ensure_return_type(type(None))
        def f():
            return None
        self.assertIsNone(f())

    def test_complex_type(self):
        @ensure_return_type(dict)
        def f():
            return {'a': 1}
        self.assertEqual(f(), {'a': 1})


if __name__ == '__main__':
    unittest.main()
