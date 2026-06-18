"""
matrix_creation.py

Exercises for creating matrices: zeros, identity, and constructing from lists.
Each exercise is a classmethod or constructor behavior implemented on Matrix.
"""
from typing import List


class Matrix:
    """Matrix creation utilities.

    Exercises:
    - zeros(rows, cols) classmethod returns a Matrix of zeros (float).
    - identity(n) classmethod returns n x n identity matrix.
    - from_list(lst) classmethod should create a Matrix from nested lists and
      validate rectangular shape.

    >>> Matrix.zeros(2, 3).shape
    (2, 3)
    >>> Matrix.identity(2).to_list()
    [[1.0, 0.0], [0.0, 1.0]]
    """

    def __init__(self, data: List[List[float]]):
        """Store deep copy of data; validate rectangular shape."""
        raise NotImplementedError

    @classmethod
    def zeros(cls, rows: int, cols: int) -> 'Matrix':
        """Return Matrix with zeros (floats)."""
        raise NotImplementedError

    @classmethod
    def identity(cls, n: int) -> 'Matrix':
        """Return n x n identity Matrix."""
        raise NotImplementedError

    @classmethod
    def from_list(cls, data: List[List[float]]) -> 'Matrix':
        """Construct Matrix from nested lists validating rectangular shape."""
        raise NotImplementedError

    def to_list(self) -> List[List[float]]:
        """Return deep-copied nested lists representing matrix."""
        raise NotImplementedError


# -------------------- Tests --------------------
import unittest


class TestZerosIdentity(unittest.TestCase):
    def test_zeros_shape(self):
        m = Matrix.zeros(3, 2)
        self.assertEqual(m.shape, (3, 2))
        self.assertTrue(all(all(v == 0.0 for v in row) for row in m.to_list()))

    def test_zeros_zero_dims(self):
        m = Matrix.zeros(0, 0)
        self.assertEqual(m.shape, (0, 0))

    def test_identity_shape(self):
        m = Matrix.identity(3)
        self.assertEqual(m.shape, (3, 3))
        lst = m.to_list()
        for i in range(3):
            for j in range(3):
                self.assertEqual(lst[i][j], 1.0 if i == j else 0.0)

    def test_identity_one(self):
        self.assertEqual(Matrix.identity(1).to_list(), [[1.0]])

    def test_identity_zero(self):
        self.assertEqual(Matrix.identity(0).to_list(), [])


class TestFromToList(unittest.TestCase):
    def test_from_list_regular(self):
        m = Matrix.from_list([[1.0, 2.0], [3.0, 4.0]])
        self.assertEqual(m.shape, (2, 2))

    def test_from_list_inconsistent(self):
        with self.assertRaises(ValueError):
            Matrix.from_list([[1.0, 2.0], [3.0]])

    def test_to_list_deep_copy(self):
        data = [[1.0]]
        m = Matrix.from_list(data)
        out = m.to_list()
        data[0][0] = 9.0
        self.assertNotEqual(out, data)

    def test_to_list_empty(self):
        self.assertEqual(Matrix.from_list([]).to_list(), [])

    def test_from_list_types(self):
        m = Matrix.from_list([[1.0, 2.0]])
        self.assertIsInstance(m.to_list(), list)


if __name__ == '__main__':
    unittest.main()
