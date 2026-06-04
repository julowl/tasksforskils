"""Exercise 2 — Find primes up to n using nested loops

Implement primes_up_to(n) that returns a list of all prime numbers <= n.
You should use for loops and a simple trial division algorithm (check divisibility
by smaller integers).
"""

from typing import List


def is_prime(num: int) -> bool:
    """Return True if num is a prime (num >= 2)."""
    if num < 2:
        return False
    # Simple trial division — check from 2 to num-1 (or up to sqrt for speed)
    raise NotImplemented


def primes_up_to(n: int) -> List[int]:
    """Return a list of primes less than or equal to n.

    Args:
        n: upper bound (inclusive)

    Returns:
        List of prime numbers in ascending order.
    """
    # TODO: use for loops to collect primes
    raise NotImplemented


if __name__ == "__main__":
    print(primes_up_to(20))  # expect [2, 3, 5, 7, 11, 13, 17, 19]
