"""
aggregators.py

Exercises about aggregation functions: receiving aggregator functions or returning them.
"""
from typing import Any, Callable, Iterable, List, Sequence


def apply_aggregator(data: list[Any], agg_fn: Callable[[Any, Any], Any]) -> Any:
    """
    Apply a user-provided aggregation function to the data and return its result.

    Examples:
    >>> apply_aggregator([1,2,3], lambda x, y: x + y)
    6

    >>> apply_aggregator([1,2,3], lambda x, y: min(x, y))
    1

    >>> apply_aggregator([1,2,3], lambda x, y: x * y)
    6

    >>> apply_aggregator([], lambda x, y: 0)
    0
    """
    if len(data) == 0:
        raise ValueError('Cannot apply aggregation to empty list')
    result = data[0]
    for x in data[1:]:
        result = agg_fn(result, x)
    return result


def make_sum_aggregator(offset: int = 0) -> Callable[[Iterable[int]], int]:
    """
    Return an aggregator function that sums integers and adds the given offset.

    Examples:
    >>> agg = make_sum_aggregator(10)
    >>> agg([1,2,3])
    16
    """
    def summ(data: Iterable[int]) -> int:
        return sum(data) + offset
    return summ



def compose_aggregators(agg1: Callable[[Iterable[Any]], Any], agg2: Callable[[Iterable[Any]], Any]) -> Callable[[Iterable[Any]], tuple]:
    """
    Return a new aggregator that returns a tuple of results from agg1 and agg2 on the same data.

    Examples:
    >>> a = compose_aggregators(sum, lambda xs: len(list(xs)))
    >>> a([1,2,3])
    (6, 3)
    """
    def new_agr(agr: Iterable[Any]):
        agr = list(agr)
        return agg1(agr), agg2(agr)
    return new_agr


# -------------------- Tests --------------------
import unittest


class TestApplyAggregator(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(apply_aggregator([1, 2, 3], sum), 6)

    def test_empty_with_default(self):
        self.assertEqual(apply_aggregator([], lambda xs: 0), 0)

    def test_join_strings(self):
        self.assertEqual(apply_aggregator(['a', 'b'], lambda xs: ''.join(xs)), 'ab')

    def test_generator(self):
        self.assertEqual(apply_aggregator((i for i in [1,2]), sum), 3)

    def test_custom_agg(self):
        self.assertEqual(apply_aggregator([1,2,3], lambda xs: max(xs)), 3)


class TestMakeSumAggregator(unittest.TestCase):
    def test_offset_zero(self):
        agg = make_sum_aggregator(0)
        self.assertEqual(agg([1,2,3]), 6)

    def test_offset_positive(self):
        agg = make_sum_aggregator(5)
        self.assertEqual(agg([1,2]), 8)

    def test_empty(self):
        agg = make_sum_aggregator(3)
        self.assertEqual(agg([]), 3)

    def test_type(self):
        self.assertTrue(callable(make_sum_aggregator()))

    def test_large(self):
        agg = make_sum_aggregator(100)
        self.assertEqual(agg([0,0,0]), 100)


class TestComposeAggregators(unittest.TestCase):
    def test_basic(self):
        a = compose_aggregators(sum, lambda xs: len(list(xs)))
        self.assertEqual(a([1,2,3]), (6, 3))

    def test_empty(self):
        a = compose_aggregators(lambda xs: 0, lambda xs: 0)
        self.assertEqual(a([]), (0, 0))

    def test_types(self):
        a = compose_aggregators(sum, max)
        res = a([1,2])
        self.assertIsInstance(res, tuple)

    def test_generator_consumption(self):
        # ensure both aggregators see the same data, so convert to tuple inside compose
        a = compose_aggregators(sum, lambda xs: len(list(xs)))
        self.assertEqual(a((i for i in [1,2,3])), (6, 3))

    def test_side_effects(self):
        def agg_count(xs):
            return sum(1 for _ in xs)

        a = compose_aggregators(sum, agg_count)
        self.assertEqual(a([1,2,3]), (6, 3))


if __name__ == '__main__':
    unittest.main()
