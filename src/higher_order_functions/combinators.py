"""
combinators.py

Exercises focused on creating combinator functions: compose, partial-like behavior, and map-like functions.
"""
from typing import Any, Callable, Iterable, List, Tuple


def compose(f: Callable[[Any], Any], g: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """
    Return a function h(x) = f(g(x)).

    Examples:
    >>> inc = lambda x: x + 1
    >>> dbl = lambda x: x * 2
    >>> h = compose(inc, dbl)
    >>> h(3)
    7
    """
    def h(x):
        return f(g(x))

    return h


def map_with(func: Callable[[Any], Any], data: Iterable[Any]) -> List[Any]:
    """
    Apply func to each element and return a list (like built-in map but returns list).

    Examples:
    >>> map_with(lambda x: x*2, [1,2,3])
    [2, 4, 6]
    """
    result = []
    for item in data:
        new_value = func(item)
        result.append(new_value)
    return result


def curry_two_arg(func: Callable[[Any, Any], Any]) -> Callable[[Any], Callable[[Any], Any]]:
    """
    Transform a two-argument function into a curried version: f(a)(b) -> func(a, b)

    Examples:
    >>> def add(a, b):
    ...     return a + b
    >>> cur = curry_two_arg(add)
    >>> cur(2)(3)
    5
    """

    def first(a):
        def second(b):
            return func(a, b)

        return second

    return first


# -------------------- Tests --------------------
import unittest


class TestCompose(unittest.TestCase):
    def test_basic(self):
        inc = lambda x: x + 1
        dbl = lambda x: x * 2
        h = compose(inc, dbl)
        self.assertEqual(h(3), 7)

    def test_string(self):
        f = lambda s: s + '!'
        g = lambda s: s.upper()
        self.assertEqual(compose(f, g)('hi'), 'HI!')

    def test_type(self):
        self.assertTrue(callable(compose(lambda x: x, lambda x: x)))

    def test_side_effects(self):
        calls: List[int] = []

        def f(x):
            calls.append(('f', x))
            return x + 1

        def g(x):
            calls.append(('g', x))
            return x * 2

        h = compose(f, g)
        self.assertEqual(h(2), 5)
        self.assertEqual(calls, [('g', 2), ('f', 4)])

    def test_none(self):
        f = lambda x: None
        g = lambda x: x
        self.assertIsNone(compose(f, g)(5))


class TestMapWith(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(map_with(lambda x: x*2, [1,2]), [2,4])

    def test_generator(self):
        self.assertEqual(map_with(str, (i for i in [1,2,3])), ['1','2','3'])

    def test_empty(self):
        self.assertEqual(map_with(lambda x: x, []), [])

    def test_side_effects(self):
        calls: List[int] = []

        def f(x):
            calls.append(x)
            return x

        self.assertEqual(map_with(f, [1,2]), [1,2])
        self.assertEqual(calls, [1,2])

    def test_types(self):
        self.assertEqual(map_with(lambda x: x+1, [0]), [1])


class TestCurryTwoArg(unittest.TestCase):
    def test_add(self):
        def add(a, b):
            return a + b

        cur = curry_two_arg(add)
        self.assertEqual(cur(2)(3), 5)

    def test_string(self):
        def join(a, b):
            return a + b

        self.assertEqual(curry_two_arg(join)('a')('b'), 'ab')

    def test_reuse(self):
        def mul(a, b):
            return a * b

        times2 = curry_two_arg(mul)(2)
        self.assertEqual(times2(5), 10)

    def test_callable(self):
        def f(a, b):
            return (a, b)

        self.assertTrue(callable(curry_two_arg(f)))

    def test_side_effects(self):
        calls: List[Tuple[str, int]] = []

        def f(a, b):
            calls.append(('f', a, b))
            return a - b

        cur = curry_two_arg(f)
        self.assertEqual(cur(5)(3), 2)
        self.assertEqual(calls, [('f', 5, 3)])


if __name__ == '__main__':
    unittest.main()
