"""
matrices_arithmetic.py

Matrix arithmetic: addition, subtraction and scalar multiplication.
All matrices are list[list[float]].
"""
from typing import List

Matrix = List[List[float]]


def add_matrices(a: Matrix, b: Matrix) -> Matrix:
    """
    Element-wise addition of two matrices of the same shape.

    Raise ValueError if shapes mismatch.

    >>> add_matrices([[1.0,2.0]], [[3.0,4.0]])
    [[4.0, 6.0]]
    """
    raise NotImplementedError


def subtract_matrices(a: Matrix, b: Matrix) -> Matrix:
    """
    Element-wise subtraction (a - b).

    Raise ValueError if shapes mismatch.
    >>> subtract_matrices([[5.0]], [[2.0]])
    [[3.0]]
    """
    raise NotImplementedError


def scalar_multiply(matrix: Matrix, scalar: float) -> Matrix:
    """
    Multiply every element of matrix by scalar and return new matrix.

    >>> scalar_multiply([[1.0, -2.0]], 2.5)
    [[2.5, -5.0]]
    """
    raise NotImplementedError


# -------------------- Tests --------------------
import unittest

class TestArithmetic(unittest.TestCase):
    def test_add_normal(self):
        self.assertEqual(add_matrices([[1.0,2.0],[3.0,4.0]], [[4.0,3.0],[2.0,1.0]]),
                         [[5.0,5.0],[5.0,5.0]])

    def test_add_shape_mismatch(self):
        try:
            add_matrices([[1.0]], [[1.0,2.0]])
        except ValueError:
            pass
        else:
            self.fail("Expected ValueError for shape mismatch")

    def test_subtract_normal(self):
        self.assertEqual(subtract_matrices([[5.0,5.0]], [[1.0,2.0]]), [[4.0,3.0]])

    def test_subtract_shape_mismatch(self):
        with self.assertRaises(ValueError):
            subtract_matrices([[1.0]], [[1.0,2.0]])

    def test_scalar_multiply(self):
        self.assertEqual(scalar_multiply([[1.0, -1.0]], 3.0), [[3.0, -3.0]])

    def test_scalar_multiply_zero(self):
        self.assertEqual(scalar_multiply([[1.0,2.0]], 0.0), [[0.0,0.0]])

if __name__ == '__main__':
    unittest.main()
