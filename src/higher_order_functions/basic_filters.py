"""
basic_filters.py

Exercises about receiving and composing predicate (filter) functions.
Each exercise requires implementing a function that works with predicates or returns them.
"""
from typing import Any, Callable, Iterable, List, Sequence


def apply_filter(data: Iterable[Any], filter_fn: Callable[[Any], bool]) -> List[Any]:
    """
    Apply a user-provided filter function to the iterable and return a list of items
    for which filter_fn(item) is True.

    Requirements:
    - Do not modify the input iterable.
    - Preserve original order.

    Examples (pydoc):
    >>> apply_filter([1, 2, 3, 4], lambda x: x % 2 == 0)
    [2, 4]

    >>> apply_filter([], lambda x: True)
    []
    """
    filter = []
    for i in data:
        if filter_fn(i):
            filter.append(i)
    return filter


def combine_filters_and_apply(data: Iterable[Any], filters: Sequence[Callable[[Any], bool]]) -> List[Any]:
    """
    Apply multiple filter functions to data. An item is kept only if every filter returns True.

    Examples:
    >>> is_even = lambda x: x % 2 == 0
    >>> gt_two = lambda x: x > 2
    >>> combine_filters_and_apply([1,2,3,4,5], [is_even, gt_two])
    [4]
    """
    filtered = data
    for filter in filters:
        filtered = apply_filter(filtered, filter)
    return filtered


def negate_filter(filter_fn: Callable[[Any], bool]) -> Callable[[Any], bool]:
    """
    Given a predicate filter_fn return a new predicate that returns the logical negation.

    Examples:
    >>> is_even = lambda x: x % 2 == 0
    >>> is_odd = negate_filter(is_even)
    >>> is_odd(3)
    True
    >>> is_odd(4)
    False
    """
    def negat(x):
       return not filter_fn(x)
    return negat


# -------------------- Tests --------------------
import unittest


class TestApplyFilter(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(apply_filter([], lambda x: True), [])

    def test_all(self):
        self.assertEqual(apply_filter([1, 2, 3], lambda x: x > 0), [1, 2, 3])

    def test_none(self):
        self.assertEqual(apply_filter([1, 2, 3], lambda x: x > 10), [])

    def test_mixed(self):
        self.assertEqual(apply_filter([0, 1, 2, 3], lambda x: x % 2 == 1), [1, 3])

    def test_non_mutating(self):
        data = [1, 2, 3]
        _ = apply_filter(data, lambda x: x > 1)
        self.assertEqual(data, [1, 2, 3])


class TestCombineFilters(unittest.TestCase):
    def test_single_filter(self):
        self.assertEqual(combine_filters_and_apply([1, 2, 3], [lambda x: x > 1]), [2, 3])

    def test_multiple_filters(self):
        self.assertEqual(combine_filters_and_apply([1, 2, 3, 4], [lambda x: x % 2 == 0, lambda x: x > 2]), [4])

    def test_no_filters(self):
        self.assertEqual(combine_filters_and_apply([1, 2], []), [1, 2])

    def test_empty_data(self):
        self.assertEqual(combine_filters_and_apply([], [lambda x: True]), [])

    def test_types(self):
        self.assertEqual(combine_filters_and_apply(['a', 'bb', 'ccc'], [lambda s: len(s) > 1]), ['bb', 'ccc'])


class TestNegateFilter(unittest.TestCase):
    def test_basic(self):
        is_even = lambda x: x % 2 == 0
        is_odd = negate_filter(is_even)
        self.assertTrue(is_odd(3))
        self.assertFalse(is_odd(4))

    def test_double_negation(self):
        f = lambda x: x > 0
        nf = negate_filter(f)
        nnf = negate_filter(nf)
        self.assertEqual(nnf(5), f(5))

    def test_side_effects(self):
        calls: List[int] = []

        def pred(x: int) -> bool:
            calls.append(x)
            return x == 1

        npred = negate_filter(pred)
        self.assertFalse(npred(1))
        self.assertTrue(npred(2))
        self.assertEqual(calls, [1, 2])

    def test_type_preservation(self):
        f = lambda x: isinstance(x, int)
        nf = negate_filter(f)
        self.assertTrue(nf('a'))
        self.assertFalse(nf(3))

    def test_callable_return(self):
        self.assertTrue(callable(negate_filter(lambda x: True)))


if __name__ == '__main__':
    unittest.main()
