"""
higher_order_inputs.py

Exercises where the user must implement functions that accept other functions (user-provided) and use them to build behavior.
"""
from typing import Any, Callable, Iterable, List, Tuple


def partition(data: Iterable[Any], predicate: Callable[[Any], bool]) -> Tuple[List[Any], List[Any]]:
    """
    Partition data into two lists: (items_where_pred_true, items_where_pred_false).

    Examples:
    >>> partition([1,2,3,4], lambda x: x%2==0)
    ([2, 4], [1, 3])
    """
    true_items = []
    false_items = []
    for item in data:
        if predicate(item):
            true_items.append(item)
        else:
            false_items.append(item)

    return (true_items, false_items)


def apply_and_aggregate(data: Iterable[Any], map_fn: Callable[[Any], Any], agg_fn: Callable[[Iterable[Any]], Any]) -> Any:
    """
    First apply map_fn to each element, then aggregate the mapped results with agg_fn.

    Examples:
    >>> apply_and_aggregate([1,2,3], lambda x: x*2, sum)
    12
    """
    result = []
    for item in data:
        result.append(map_fn(item))
    return agg_fn(result)


def filter_map_reduce(data: Iterable[Any], filter_fn: Callable[[Any], bool], map_fn: Callable[[Any], Any], reduce_fn: Callable[[Any, Any], Any], initial: Any) -> Any:
    """
    Typical pipeline: filter -> map -> reduce. Return the reduced value starting from initial.

    Examples:
    >>> from operator import add
    >>> filter_map_reduce([1,2,3,4], lambda x: x%2==0, lambda x: x*10, add, 0)
    60
    """
    def reduce(items: list[Any]):
        first = initial
        for item in items:
            first = reduce_fn(first, item)
        return first

    filtered, _ = partition(data, filter_fn)

    mapped = apply_and_aggregate(filtered, map_fn, reduce)

    return mapped


# -------------------- Tests --------------------
import unittest


class TestPartition(unittest.TestCase):
    def test_basic(self):
        evens, odds = partition([1,2,3,4], lambda x: x%2==0)
        self.assertEqual(evens, [2,4])
        self.assertEqual(odds, [1,3])

    def test_all_true(self):
        a, b = partition([1,2], lambda x: True)
        self.assertEqual(a, [1,2])
        self.assertEqual(b, [])

    def test_all_false(self):
        a, b = partition([], lambda x: True)
        self.assertEqual(a, [])
        self.assertEqual(b, [])

    def test_types(self):
        a, b = partition(['a','bb','ccc'], lambda s: len(s)>1)
        self.assertEqual(a, ['bb','ccc'])

    def test_generator(self):
        a, b = partition((i for i in [1,2,3]), lambda x: x>1)
        self.assertEqual(a, [2,3])


class TestApplyAndAggregate(unittest.TestCase):
    def test_sum_doubles(self):
        self.assertEqual(apply_and_aggregate([1,2,3], lambda x: x*2, sum), 12)

    def test_join(self):
        self.assertEqual(apply_and_aggregate([1,2], lambda x: str(x), lambda xs: '-'.join(xs)), '1-2')

    def test_empty(self):
        self.assertEqual(apply_and_aggregate([], lambda x: x, lambda xs: 0), 0)

    def test_generator(self):
        self.assertEqual(apply_and_aggregate((i for i in [1,2]), lambda x: x+1, sum), 5)

    def test_side_effects(self):
        calls: List[int] = []

        def f(x):
            calls.append(x)
            return x

        apply_and_aggregate([1,2], f, sum)
        self.assertEqual(calls, [1,2])


class TestFilterMapReduce(unittest.TestCase):
    def test_basic(self):
        from operator import add
        self.assertEqual(filter_map_reduce([1,2,3,4], lambda x: x%2==0, lambda x: x*10, add, 0), 60)

    def test_initial(self):
        from operator import mul
        self.assertEqual(filter_map_reduce([2,3], lambda x: True, lambda x: x, lambda a,b: a*b, 1), 6)

    def test_empty(self):
        from operator import add
        self.assertEqual(filter_map_reduce([], lambda x: True, lambda x: x, add, 0), 0)

    def test_types(self):
        from operator import add
        self.assertEqual(filter_map_reduce(['a','bb'], lambda s: True, lambda s: len(s), add, 0), 3)

    def test_generator(self):
        from operator import add
        self.assertEqual(filter_map_reduce((i for i in [1,2,3]), lambda x: x>1, lambda x: x*2, add, 0), 10)


if __name__ == '__main__':
    unittest.main()
