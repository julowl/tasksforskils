"""
matrix_indexing.py

Exercises about indexing and row/column extraction for a Matrix class.
Students will implement __getitem__, __setitem__, and row/col access methods.
"""
from typing import List, Tuple


class Matrix:
    """Matrix indexing exercises.

    Requirements:
    - __init__(data)
    - __getitem__(idx): if idx is int return row as list[float], if tuple (r,c) return element.
    - __setitem__(idx, value): allow setting element at (r,c) using matrix[r, c] = v
    - row(r) and col(c) methods returning copies of the row/column.

    >>> m = Matrix([[1.0,2.0],[3.0,4.0]])
    >>> m[0]
    [1.0, 2.0]
    >>> m[1,1]
    4.0
    """

    def __init__(self, data: List[List[float]]):
        """Store deep copy and validate rectangular shape."""
        raise NotImplementedError

    def __getitem__(self, idx):
        """Support m[row] -> List[float] and m[row, col] -> float."""
        raise NotImplementedError

    def __setitem__(self, idx, value: float) -> None:
        """Support setting single element m[row, col] = value."""
        raise NotImplementedError

    def row(self, r: int) -> List[float]:
        """Return a deep-copied list for the r-th row."""
        raise NotImplementedError

    def col(self, c: int) -> List[float]:
        """Return a deep-copied list for the c-th column."""
        raise NotImplementedError


# -------------------- Tests --------------------
import unittest


class TestIndexing(unittest.TestCase):
    def setUp(self):
        self.m = Matrix([[1.0, 2.0], [3.0, 4.0]])

    def test_get_row(self):
        self.assertEqual(self.m[0], [1.0, 2.0])

    def test_get_element(self):
        self.assertEqual(self.m[1, 1], 4.0)

    def test_set_element(self):
        self.m[0, 1] = 9.0
        self.assertEqual(self.m[0, 1], 9.0)

    def test_set_invalid_index(self):
        with self.assertRaises(IndexError):
            self.m[10, 10] = 1.0

    def test_get_invalid_index(self):
        with self.assertRaises(IndexError):
            _ = self.m[5]


class TestRowCol(unittest.TestCase):
    def setUp(self):
        self.m = Matrix([[1.0, 2.0], [3.0, 4.0]])

    def test_row_copy(self):
        r = self.m.row(0)
        r[0] = 99.0
        self.assertEqual(self.m[0, 0], 1.0)

    def test_col_copy(self):
        c = self.m.col(1)
        c[0] = 99.0
        self.assertEqual(self.m[0, 1], 2.0)

    def test_row_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.m.row(5)

    def test_col_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.m.col(5)

    def test_row_and_col_lengths(self):
        self.assertEqual(len(self.m.row(0)), 2)
        self.assertEqual(len(self.m.col(0)), 2)


if __name__ == '__main__':
    unittest.main()
