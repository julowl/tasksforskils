"""Exercise 4 — Recursion

Implement factorial and fibonacci using recursion.

Both functions should validate input and raise ValueError for negative inputs.

Do not import or use iterative implementations here — the goal is practice with recursion.
"""


def factorial(n: int) -> int:
    """Return n! (n factorial) computed recursively.

    Args:
        n: non-negative integer

    Returns:
        n! as an integer

    Raises:
        ValueError: if n < 0
    """
    raise NotImplemented


def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number, with fibonacci(0) == 0 and fibonacci(1) == 1.

    Args:
        n: non-negative integer index in the Fibonacci sequence

    Returns:
        Fibonacci number at position n

    Raises:
        ValueError: if n < 0
    """
    raise NotImplemented


# --- Tests for exercise 4 ---

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(6) == 8


def test_negative_inputs():
    import pytest

    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(ValueError):
        fibonacci(-5)


if __name__ == '__main__':
    test_factorial()
    test_fibonacci()
    print('ex4_recursion: tests passed (quick)')
