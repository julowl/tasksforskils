"""
matrix_basic.py

Exercises covering basic Matrix class construction and simple properties.
Students will implement __init__, shape property, and is_square method.
"""
from typing import List, Tuple


class Matrix:
    """Simple Matrix class backed by a list of lists of floats.

    Requirements (exercises):
    - __init__ should accept data: List[List[float]] and validate that all rows
      have the same length or raise ValueError. A deep copy should be stored.
    - shape property should return (rows, cols).
    - is_square() method should return True for n x n matrices.

    >>> Matrix([[1.0, 2.0], [3.0, 4.0]]).shape
    (2, 2)
    >>> Matrix([]).shape
    (0, 0)
    >>> Matrix([[1.0]]).is_square()
    True
    """

    def __init__(self, data: List[List[float]]):
        """Initialize matrix with deep-copied data and validate rectangular shape.

        Raise ValueError for rows of differing lengths.
        """
        first_len = len(data[0])
        copied = []
        for row in data:
            if len(row) != first_len:
                raise ValueError
            copied.append(row[:])
        self.data = copied

    @property
    def shape(self) -> Tuple[int, int]:
        """Return (rows, cols). Empty matrix [] has shape (0,0)."""
        if not self.data:
            return (0, 0)

        rows = len(self.data)
        cols = len(self.data[0])

        return (rows, cols)


    def is_square(self) -> bool:
        """Return True if matrix is square (n x n)."""
        raise NotImplementedError


# -------------------- Tests --------------------
import unittest


class TestMatrixInit(unittest.TestCase):
    def test_init_regular(self):
        m = Matrix([[1.0, 2.0], [3.0, 4.0]])
        self.assertEqual(m.shape, (2, 2))

    def test_init_empty(self):
        m = Matrix([])
        self.assertEqual(m.shape, (0, 0))

    def test_init_inconsistent_rows(self):
        with self.assertRaises(ValueError):
            Matrix([[1.0, 2.0], [3.0]])

    def test_init_deep_copy(self):
        data = [[1.0]]
        m = Matrix(data)
        data[0][0] = 5.0
        # deep copy required: original change should not affect Matrix
        self.assertEqual(m.shape, (1, 1))
        self.assertNotEqual(m.__dict__.get('data', None), data)

    def test_init_types(self):
        # allow empty rows list
        m = Matrix([])
        self.assertIsInstance(m.shape, tuple)


class TestShapeIsSquare(unittest.TestCase):
    def test_shape_normal(self):
        self.assertEqual(Matrix([[1.0, 2.0], [3.0, 4.0]]).shape, (2, 2))

    def test_shape_single(self):
        self.assertEqual(Matrix([[1.0]]).shape, (1, 1))

    def test_is_square_true(self):
        self.assertTrue(Matrix([[1.0, 2.0], [3.0, 4.0]]).is_square())

    def test_is_square_false(self):
        self.assertFalse(Matrix([[1.0, 2.0, 3.0]]).is_square())

    def test_is_square_empty(self):
        # empty is not square
        self.assertFalse(Matrix([]).is_square())


if __name__ == '__main__':
    unittest.main()
