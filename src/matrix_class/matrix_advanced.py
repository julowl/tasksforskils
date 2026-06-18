"""
matrix_advanced.py

Advanced matrix operations: transpose, trace, and determinant (recursive).
Students will implement these as instance methods.
"""
from typing import List


class Matrix:
    """Advanced matrix exercises.

    Exercises:
    - transpose() -> Matrix
    - trace() -> float (only for square matrices, ValueError otherwise)
    - determinant() -> float for square matrices (use recursive expansion)

    >>> Matrix([[1.0,2.0],[3.0,4.0]]).transpose().to_list()
    [[1.0, 3.0], [2.0, 4.0]]
    """

    def __init__(self, data: List[List[float]]):
        """Store deep copy and validate rectangular shape."""
        raise NotImplementedError

    def transpose(self) -> 'Matrix':
        """Return a new Matrix that is the transpose."""
        raise NotImplementedError

    def trace(self) -> float:
        """Return the sum of diagonal elements. Raise ValueError if not square."""
        raise NotImplementedError

    def determinant(self) -> float:
        """Return determinant (recursive). Raise ValueError if not square."""
        raise NotImplementedError

    def to_list(self) -> List[List[float]]:
        raise NotImplementedError


# -------------------- Tests --------------------
import unittest


class TestTransposeTrace(unittest.TestCase):
    def test_transpose_2x2(self):
        m = Matrix([[1.0, 2.0], [3.0, 4.0]])
        self.assertEqual(m.transpose().to_list(), [[1.0, 3.0], [2.0, 4.0]])

    def test_transpose_non_square(self):
        m = Matrix([[1.0, 2.0, 3.0]])
        self.assertEqual(m.transpose().to_list(), [[1.0], [2.0], [3.0]])

    def test_trace_square(self):
        self.assertEqual(Matrix([[1.0, 2.0], [3.0, 4.0]]).trace(), 5.0)

    def test_trace_not_square(self):
        with self.assertRaises(ValueError):
            Matrix([[1.0, 2.0, 3.0]]).trace()

    def test_transpose_empty(self):
        self.assertEqual(Matrix([]).transpose().to_list(), [])


class TestDeterminant(unittest.TestCase):
    def test_det_1x1(self):
        self.assertEqual(Matrix([[5.0]]).determinant(), 5.0)

    def test_det_2x2(self):
        self.assertEqual(Matrix([[1.0, 2.0], [3.0, 4.0]]).determinant(), -2.0)

    def test_det_3x3(self):
        m = Matrix([[6.0,1.0,1.0],[4.0,-2.0,5.0],[2.0,8.0,7.0]])
        self.assertEqual(round(m.determinant(), 6), -306.0)

    def test_det_not_square(self):
        with self.assertRaises(ValueError):
            Matrix([[1.0, 2.0]]).determinant()

    def test_det_empty(self):
        with self.assertRaises(ValueError):
            Matrix([]).determinant()


if __name__ == '__main__':
    unittest.main()
