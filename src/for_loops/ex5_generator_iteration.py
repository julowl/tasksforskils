"""Exercise 5 — Create a generator that yields chunks using for loops

Implement chunked(iterable, n) that yields consecutive chunks (lists) of size n
from the iterable. The last chunk may be smaller if there are not enough items.

Use a for loop to collect items into a buffer and yield when full.
"""

from typing import Iterable, Iterator, List, TypeVar

T = TypeVar('T')


def chunked(iterable: Iterable[T], n: int) -> Iterator[List[T]]:
    """Yield lists of up to n items from iterable.

    Args:
        iterable: an iterable of items
        n: chunk size (n > 0)

    Yields:
        Lists with up to n items in order.
    """
    # Implement using a for loop and yield
    raise NotImplemented


if __name__ == "__main__":
    for c in chunked(range(10), 3):
        print(c)
