"""Higher-order functions: functions taking and returning functions.

Exercises include composing functions, applying functions multiple times, and factories.

Theory:
- Higher-order functions accept or return other functions; they enable abstraction and reuse.
- Composition applies one function to the result of another: f(g(x)).
- Factories (closures) can produce specialized functions (e.g., multipliers) without repeating logic.
"""
from typing import Callable, TypeVar

T = TypeVar('T')
U = TypeVar('U')


def apply_twice(func: Callable[[T], T], value: T) -> T:
    """Apply func to value two times: func(func(value)).

    Requirements:
    - Return func(func(value)).

    Examples:
    >>> apply_twice(lambda x: x + 1, 3)
    5
    """
    return func(func(value))



def compose(f: Callable[[U], T], g: Callable[[T], U]) -> Callable[[T], T]:
    """Return a new function h such that h(x) == f(g(x)).

    Requirements:
    - The returned function should accept one argument and apply g then f.

    Examples:
    >>> h = compose(lambda x: x * 2, lambda x: x + 3)
    >>> h(4)
    14
    """
    def h(x: T) -> T:
        return f(g(x))
    return h


def make_multiplier(n: int) -> Callable[[int], int]:
    """Return a function that multiplies its integer argument by n.

    Examples:
    >>> doubler = make_multiplier(2)
    >>> doubler(3)
    6
    """
    def f(num:int) -> int:
        return num * n
    return f


# -------------------- Tests --------------------
import unittest


class TestApplyTwice(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(apply_twice(lambda x: x + 1, 1), 3)

    def test_square(self):
        self.assertEqual(apply_twice(lambda x: x * x, 2), 16)

    def test_string(self):
        self.assertEqual(apply_twice(lambda s: s + '!', 'hi'), 'hi!!')

    def test_identity(self):
        self.assertEqual(apply_twice(lambda x: x, 5), 5)

    def test_complex(self):
        self.assertEqual(apply_twice(lambda x: x * 2 + 1, 1), 7)


class TestCompose(unittest.TestCase):
    def test_basic(self):
        h = compose(lambda x: x * 2, lambda x: x + 1)
        self.assertEqual(h(3), 8)

    def test_string(self):
        h = compose(lambda s: s.upper(), lambda s: s + '!')
        self.assertEqual(h('a'), 'A!')

    def test_nested(self):
        h = compose(lambda x: x - 1, lambda x: x * 3)
        self.assertEqual(h(2), 5)

    def test_return_type(self):
        h = compose(lambda x: str(x), lambda x: x + 1)
        self.assertEqual(h(4), '5')

    def test_side_effect_free(self):
        h = compose(lambda x: x + 0, lambda x: x)
        self.assertEqual(h(10), 10)


class TestMakeMultiplier(unittest.TestCase):
    def test_double(self):
        f = make_multiplier(2)
        self.assertEqual(f(5), 10)

    def test_zero(self):
        f = make_multiplier(0)
        self.assertEqual(f(10), 0)

    def test_negative(self):
        f = make_multiplier(-1)
        self.assertEqual(f(3), -3)

    def test_independence(self):
        a = make_multiplier(2)
        b = make_multiplier(3)
        self.assertEqual(a(4), 8)
        self.assertEqual(b(4), 12)

    def test_large(self):
        self.assertEqual(make_multiplier(1000)(2), 2000)


if __name__ == '__main__':
    unittest.main()
