"""Exercise 3 — Higher-order functions and closures

Implement functions that take or return other functions.

Use the provided docstrings; raise NotImplemented where the implementation is required.
"""

from typing import Callable


def apply_twice(func: Callable[[int], int], x: int) -> int:
    """Apply function func to x two times: func(func(x)).

    Args:
        func: a function that accepts one integer and returns an integer
        x: input integer

    Returns:
        Result of applying func twice
    """
    raise NotImplemented


def make_multiplier(n: int) -> Callable[[int], int]:
    """Return a new function that multiplies its input by n.

    Example:
        double = make_multiplier(2)
        double(5) == 10

    Args:
        n: multiplier factor

    Returns:
        A function f(x) that returns x * n
    """
    raise NotImplemented


# --- Tests for exercise 3 ---

def test_apply_twice_and_multiplier():
    def plus_one(x):
        return x + 1

    assert apply_twice(plus_one, 3) == 5  # plus_one(plus_one(3)) => 5

    triple = make_multiplier(3)
    assert callable(triple)
    assert triple(4) == 12


if __name__ == '__main__':
    test_apply_twice_and_multiplier()
    print('ex3_higher_order: tests passed (quick)')
