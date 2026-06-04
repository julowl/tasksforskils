"""Exercise 5 — Decorators

Implement two decorators: memoize and retry.

- memoize should cache results by arguments (simple positional args is fine).
- retry(times) should retry a failing call up to times times before re-raising the exception.

Placeholders use 'raise NotImplemented'.
"""

from functools import wraps
from typing import Callable


def memoize(func: Callable) -> Callable:
    """A simple memoization decorator for functions with positional arguments.

    The decorated function should store results in a cache and return cached values
    for identical calls.

    Args:
        func: the function to decorate

    Returns:
        The wrapped function with caching behavior
    """
    raise NotImplemented


def retry(times: int = 3) -> Callable:
    """Return a decorator that retries the decorated function up to `times` times
    if it raises an exception. On last failure, re-raise the exception.

    Args:
        times: maximum number of attempts (must be >= 1)

    Returns:
        A decorator
    """
    raise NotImplemented


# --- Tests for exercise 5 ---

def test_memoize_caches_results():
    calls = {'count': 0}

    @memoize
    def f(x):
        calls['count'] += 1
        return x * 2

    assert f(2) == 4
    assert f(2) == 4
    # Second call should be cached, so count should still be 1
    assert calls['count'] == 1


def test_retry_success_after_failures():
    state = {'attempts': 0}

    @retry(times=3)
    def sometimes_fails():
        state['attempts'] += 1
        if state['attempts'] < 3:
            raise ValueError('fail')
        return 'ok'

    assert sometimes_fails() == 'ok'
    assert state['attempts'] == 3


def test_retry_final_failure():
    import pytest

    @retry(times=2)
    def always_fails():
        raise RuntimeError('nope')

    with pytest.raises(RuntimeError):
        always_fails()


if __name__ == '__main__':
    print('Run tests with pytest for detailed output')
