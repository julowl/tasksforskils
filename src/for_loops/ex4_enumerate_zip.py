"""Exercise 4 — Work with enumerate and zip in loops

Implement two small helpers:
- index_items(items): return a list of strings "{index}:{item}" using enumerate
- combine_lists(a, b): return a list of tuples pairing elements with zip
"""

from typing import Iterable, List, Tuple


def index_items(items: Iterable[object]) -> List[str]:
    """Return a list of "index:item" strings for the iterable using enumerate.

    Example: index_items(['a','b']) -> ['0:a', '1:b']
    """
    raise NotImplemented


def combine_lists(a: Iterable[object], b: Iterable[object]) -> List[Tuple[object, object]]:
    """Return list of tuples pairing elements from a and b using zip.

    The result length should be the length of the shorter iterable.
    """
    raise NotImplemented


if __name__ == "__main__":
    print(index_items(['x', 'y']))
    print(combine_lists([1,2],["a","b","c"]))
