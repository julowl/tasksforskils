"""
matrices_basic.py

Basic utilities for matrix represented as list[list[float]].
Provides functions to get shape, check square, and create zero matrix.
"""
from typing import List, Tuple

Matrix = List[List[float]]


def shape(matrix: Matrix) -> Tuple[int, int]:
    """
    Return the shape of the matrix as (rows, cols).

    >>> shape([[1.0, 2.0], [3.0, 4.0]])
    (2, 2)

    >>> shape([])
    (0, 0)
    """
    raise NotImplementedError


def is_square(matrix: Matrix) -> bool:
    """
    Return True if matrix is square (n x n), False otherwise.

    >>> is_square([[1.0]])
    True

    >>> is_square([[1.0, 2.0]])
    False
    """
    raise NotImplementedError


def zeros(rows: int, cols: int) -> Matrix:
    """
    Create a rows x cols zero matrix (floats).

    >>> zeros(2, 3)
    [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
    """
    raise NotImplementedError


# -------------------- Tests --------------------
import unittest

class TestBasic(unittest.TestCase):
    def test_shape_regular(self):
        self.assertEqual(shape([[1.0, 2.0], [3.0, 4.0]]), (2,2))

    def test_shape_empty(self):
        self.assertEqual(shape([]), (0,0))

    def test_is_square_true(self):
        self.assertTrue(is_square([[1.0, 2.0], [3.0, 4.0]]))

    def test_is_square_false(self):
        self.assertFalse(is_square([[1.0, 2.0, 3.0]]))

    def test_zeros_shape(self):
        z = zeros(3,2)
        self.assertEqual(len(z), 3)
        self.assertEqual(len(z[0]), 2)
        self.assertTrue(all(all(abs(x) < 1e-9 for x in row) for row in z))

    def test_zeros_zero_rows(self):
        z = zeros(0, 0)
        self.assertEqual(z, [])

if __name__ == '__main__':
    unittest.main()
