"""Exercise 1 — Basic function definitions

Implement the two simple functions below. Keep implementations small and follow the docstrings.

Each implementation should raise NotImplemented until filled in.

Tests are included at the bottom of this file. Run with pytest.
"""

from typing import Any


def add(a: float, b: float) -> float:
    """Return the sum of a and b.

    Args:
        a: first addend
        b: second addend

    Returns:
        The numeric sum a + b
    """
    return a + b



def repeat(s: str, n: int = 1) -> str:
    """Return the string s repeated n times.

    If n <= 0 return an empty string.

    Args:
        s: input string
        n: number of repetitions

    Returns:
        The repeated string
    """
    # s == "a" n == 5
    if n <= 0:
        return ""
    result = ""
    for _ in range(n):
        result = result+s
    return result


# --- Tests for exercise 1 ---

def test_add():
    assert add(1, 2) == 3
    assert abs(add(2.5, 0.5) - 3.0) < 1e-9


def test_repeat():
    assert repeat('a', 3) == 'aaa'
    assert repeat('x', 0) == ''
    assert repeat('hi', 1) == 'hi'


if __name__ == '__main__':
    # Quick run of tests if executed directly
    test_add()
    test_repeat()
    print('ex1_basic: tests passed (quick)')
