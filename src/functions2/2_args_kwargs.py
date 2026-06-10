"""Exercises on positional arguments, *args and **kwargs.

Students will implement variadic functions, merging dicts, and calling functions with kwargs.

Theory:
- *args collects extra positional arguments into a tuple; **kwargs collects extra
  keyword arguments into a dict.
- Default parameter values provide optional arguments; keyword-only parameters
  make calls explicit.
- When merging dictionaries avoid mutating inputs; later mappings override earlier ones.
"""
from typing import Any, Callable, Dict



def merge_dicts(*dicts: Dict[Any, Any]) -> Dict[Any, Any]:
    """Merge multiple dictionaries into one.

    Requirements:
    - Later dictionaries override earlier ones on key conflicts.
    - Return a new dictionary and do not mutate inputs.

    Examples:
    >>> merge_dicts({1: 'a'}, {1: 'b', 2: 'c'})
    {1: 'b', 2: 'c'}
    """
    new_dict = {}
    for dict in dicts:
        for key in dict:
            new_dict[key] = dict[key]
    return new_dict


def call_with_kwargs(func: Callable[..., Any], **kwargs: Any) -> Any:
    """Call func with provided keyword arguments and return the result.

    Requirements:
    - Simply call func(**kwargs) and return its result.

    Examples:
    >>> def f(x=1, y=2):
    ...     return x + y
    >>> call_with_kwargs(f, x=3, y=4)
    7
    """
    return func(**kwargs)


# -------------------- Tests --------------------
import unittest


class TestMergeDicts(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(merge_dicts({1: 'a'}, {2: 'b'}), {1: 'a', 2: 'b'})

    def test_override(self):
        self.assertEqual(merge_dicts({1: 'a'}, {1: 'b'}), {1: 'b'})

    def test_multiple(self):
        self.assertEqual(merge_dicts({1: 1}, {2: 2}, {1: 'x'}), {1: 'x', 2: 2})

    def test_original_unchanged(self):
        a = {1: 'a'}
        b = {2: 'b'}
        _ = merge_dicts(a, b)
        self.assertEqual(a, {1: 'a'})
        self.assertEqual(b, {2: 'b'})

    def test_empty(self):
        self.assertEqual(merge_dicts(), {})


class TestCallWithKwargs(unittest.TestCase):
    def test_simple(self):
        def f(x=0, y=0):
            return x + y
        self.assertEqual(call_with_kwargs(f, x=5, y=6), 11)

    def test_missing_kw(self):
        def f(a=1):
            return a
        self.assertEqual(call_with_kwargs(f), 1)

    def test_extra_kw(self):
        def f(**kwargs):
            return kwargs
        self.assertEqual(call_with_kwargs(f, x=1, y=2), {'x': 1, 'y': 2})

    def test_non_callable(self):
        with self.assertRaises(TypeError):
            call_with_kwargs(123)  # type: ignore

    def test_returns_none(self):
        def f():
            return None
        self.assertIsNone(call_with_kwargs(f))


if __name__ == '__main__':
    unittest.main()
