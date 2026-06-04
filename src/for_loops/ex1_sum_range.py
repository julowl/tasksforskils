"""Exercise 1 — Sum numbers in a range using for and range

Implement sum_in_range(start, end, step=1) which returns the sum of the
integers produced by range(start, end+1, step).

Notes:
- The function should work when start <= end and when step is positive.
- You should use a for loop and the range built-in.
"""

from typing import Optional


def sum_in_range(start: int, end: int, step: int = 1) -> int:
    """Return the sum of integers from start to end inclusive stepping by step.

    Args:
        start: first integer
        end: last integer (inclusive)
        step: step size (positive)

    Returns:
        The integer sum of the selected values.
    """
    summ = 0
    for i in range(start, end+1, step):
        summ += i
    return summ


if __name__ == "__main__":
    print(sum_in_range(1, 5))  # expect 15
