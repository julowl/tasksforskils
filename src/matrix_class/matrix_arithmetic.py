"""
matrix_arithmetic.py

Exercises for implementing arithmetic operations on Matrix classes: addition,
subtraction and scalar multiplication/operators.
"""
from typing import List


class Matrix:
    """Arithmetic on matrices.

    Exercises:
    - __init__(data)
    - __add__(other) element-wise add, raise ValueError for shape mismatch
    - __sub__(other) element-wise subtract
    - scalar_multiply(scalar) and __mul__ to support matrix * scalar

    >>> Matrix([[1.0,2.0]]) + Matrix([[3.0,4.0]])
    [[4.0, 6.0]]
    >>> Matrix([[1.0,2.0]]) * 2.0
    [[2.0, 4.0]]
    """

    def __init__(self, data: List[List[float]]):
        """Store deep copy and validate rectangular shape."""
        raise NotImplementedError

    def _shape(self):
        raise NotImplementedError

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """Element-wise addition. Raise ValueError for shape mismatch."""
        raise NotImplementedError

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        """Element-wise subtraction."""
        raise NotImplementedError

    def scalar_multiply(self, scalar: float) -> 'Matrix':
        """Return new Matrix with every element multiplied by scalar."""
        raise NotImplementedError

    def __mul__(self, scalar: float) -> 'Matrix':
        """Support matrix * scalar."""
        raise NotImplementedError

    def to_list(self) -> List[List[float]]:
        """Return deep-copied nested list representation."""
        raise NotImplementedError


# -------------------- Tests --------------------
import unittest


class TestAddSubtract(unittest.TestCase):
    def test_add_normal(self):
        a = Matrix([[1.0, 2.0], [3.0, 4.0]])
        b = Matrix([[4.0, 3.0], [2.0, 1.0]])
        out = a + b
        self.assertEqual(out.to_list(), [[5.0, 5.0], [5.0, 5.0]])

    def test_add_shape_mismatch(self):
        a = Matrix([[1.0]])
        b = Matrix([[1.0, 2.0]])
        with self.assertRaises(ValueError):
            _ = a + b

    def test_subtract_normal(self):
        a = Matrix([[5.0, 5.0]])
        b = Matrix([[1.0, 2.0]])
        out = a - b
        self.assertEqual(out.to_list(), [[4.0, 3.0]])

    def test_subtract_shape_mismatch(self):
        with self.assertRaises(ValueError):
            _ = Matrix([[1.0]]) - Matrix([[1.0, 2.0]])

    def test_add_empty(self):
        with self.assertRaises(ValueError):
            _ = Matrix([]) + Matrix([])


class TestScalarMultiply(unittest.TestCase):
    def test_scalar_multiply(self):
        m = Matrix([[1.0, -1.0]])
        out = m.scalar_multiply(3.0)
        self.assertEqual(out.to_list(), [[3.0, -3.0]])

    def test_mul_operator(self):
        m = Matrix([[1.0, 2.0]])
        self.assertEqual((m * 2.0).to_list(), [[2.0, 4.0]])

    def test_scalar_zero(self):
        self.assertEqual(Matrix([[1.0, 2.0]]).scalar_multiply(0.0).to_list(), [[0.0, 0.0]])

    def test_scalar_negative(self):
        self.assertEqual(Matrix([[2.0]]).scalar_multiply(-1.0).to_list(), [[-2.0]])

    def test_scalar_leaves_original(self):
        m = Matrix([[1.0]])
        _ = m.scalar_multiply(2.0)
        self.assertEqual(m.to_list(), [[1.0]])


if __name__ == '__main__':
    unittest.main()
