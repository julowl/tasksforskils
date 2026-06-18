"""
matrix_multiplication.py

Exercises for matrix multiplication-related operations: matmul, vector multiply,
and Hadamard (element-wise) product.
"""
from typing import List


class Matrix:
    """Matrix multiplication exercises.

    Exercises:
    - __init__(data)
    - matmul(other) and __matmul__ operator for matrix multiplication
    - multiply_vector(vec) multiply matrix by a vector (list[float])
    - hadamard(other) element-wise product (shape must match)

    >>> Matrix([[1.0, 2.0], [3.0, 4.0]]) @ Matrix([[5.0,6.0],[7.0,8.0]])
    [[19.0, 22.0], [43.0, 50.0]]
    """

    def __init__(self, data: List[List[float]]):
        """Store deep copy and validate rectangular shape."""
        raise NotImplementedError

    def shape(self):
        raise NotImplementedError

    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        """Matrix multiplication. Raise ValueError on incompatible shapes."""
        raise NotImplementedError

    def multiply_vector(self, vec: List[float]) -> List[float]:
        """Multiply matrix by column vector (list) returning a list of floats."""
        raise NotImplementedError

    def hadamard(self, other: 'Matrix') -> 'Matrix':
        """Element-wise product (same shape)."""
        raise NotImplementedError

    def to_list(self) -> List[List[float]]:
        raise NotImplementedError


# -------------------- Tests --------------------
import unittest


class TestMatmul(unittest.TestCase):
    def test_matmul_regular(self):
        a = Matrix([[1.0, 2.0], [3.0, 4.0]])
        b = Matrix([[5.0, 6.0], [7.0, 8.0]])
        res = a @ b
        self.assertEqual(res.to_list(), [[19.0, 22.0], [43.0, 50.0]])

    def test_matmul_incompatible(self):
        a = Matrix([[1.0, 2.0]])
        b = Matrix([[1.0, 2.0]])
        with self.assertRaises(ValueError):
            _ = a @ b

    def test_matmul_with_identity(self):
        a = Matrix([[1.0, 2.0], [3.0, 4.0]])
        identity = Matrix([[1.0, 0.0], [0.0, 1.0]])
        self.assertEqual((a @ identity).to_list(), a.to_list())

    def test_matmul_empty(self):
        with self.assertRaises(ValueError):
            Matrix([]) @ Matrix([])

    def test_matmul_non_square(self):
        a = Matrix([[1.0, 2.0, 3.0]])
        b = Matrix([[1.0], [2.0], [3.0]])
        res = a @ b
        self.assertEqual(res.to_list(), [[14.0]])


class TestVectorAndHadamard(unittest.TestCase):
    def test_multiply_vector(self):
        a = Matrix([[1.0, 2.0], [3.0, 4.0]])
        v = [1.0, 1.0]
        self.assertEqual(a.multiply_vector(v), [3.0, 7.0])

    def test_multiply_vector_size_mismatch(self):
        with self.assertRaises(ValueError):
            Matrix([[1.0, 2.0]]).multiply_vector([1.0])

    def test_hadamard_regular(self):
        a = Matrix([[1.0, 2.0], [3.0, 4.0]])
        b = Matrix([[2.0, 0.5], [1.0, -1.0]])
        self.assertEqual(a.hadamard(b).to_list(), [[2.0, 1.0], [3.0, -4.0]])

    def test_hadamard_shape_mismatch(self):
        with self.assertRaises(ValueError):
            Matrix([[1.0]]).hadamard(Matrix([[1.0, 2.0]]))

    def test_vector_mult_single(self):
        self.assertEqual(Matrix([[2.0]]).multiply_vector([3.0]), [6.0])


if __name__ == '__main__':
    unittest.main()
