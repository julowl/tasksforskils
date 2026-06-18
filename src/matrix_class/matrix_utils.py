"""
matrix_utils.py

Utility-like operations for Matrix class: equality, approximate equality,
and converting to list (deep copy). These are small exercises focusing on
comparison and tolerances.
"""
from typing import List


class Matrix:
    """Utility exercises.

    Exercises:
    - __init__(data)
    - __eq__(other) exact equality
    - approx_equal(other, tol=1e-9) approximate equality for floats
    - to_list() return deep-copy nested lists

    >>> Matrix([[1.0]]).__eq__(Matrix([[1.0]]))
    True
    """

    def __init__(self, data: List[List[float]]):
        """Store deep copy and validate rectangular shape."""
        raise NotImplementedError

    def __eq__(self, other: 'Matrix') -> bool:
        """Return True if shapes and all corresponding elements are exactly equal."""
        raise NotImplementedError

    def approx_equal(self, other: 'Matrix', tol: float = 1e-9) -> bool:
        """Return True if shapes match and all elements differ by at most tol."""
        raise NotImplementedError

    def to_list(self) -> List[List[float]]:
        """Return deep-copied nested lists representing the matrix."""
        raise NotImplementedError


# -------------------- Tests --------------------
import unittest


class TestEq(unittest.TestCase):
    def test_eq_true(self):
        self.assertTrue(Matrix([[1.0, 2.0]]) == Matrix([[1.0, 2.0]]))

    def test_eq_false(self):
        self.assertFalse(Matrix([[1.0]]) == Matrix([[2.0]]))

    def test_eq_shape_mismatch(self):
        self.assertFalse(Matrix([[1.0]]) == Matrix([[1.0, 2.0]]))

    def test_eq_empty(self):
        self.assertTrue(Matrix([]) == Matrix([]))

    def test_eq_type(self):
        self.assertFalse(Matrix([[1.0]]) == object())


class TestApproxEqual(unittest.TestCase):
    def test_approx_equal_true(self):
        a = Matrix([[1.0, 2.0000000001]])
        b = Matrix([[1.0, 2.0]])
        self.assertTrue(a.approx_equal(b, tol=1e-9))

    def test_approx_equal_false(self):
        a = Matrix([[1.0, 2.1]])
        b = Matrix([[1.0, 2.0]])
        self.assertFalse(a.approx_equal(b, tol=1e-3))

    def test_approx_shape_mismatch(self):
        self.assertFalse(Matrix([[1.0]]).approx_equal(Matrix([[1.0, 2.0]])))

    def test_approx_empty(self):
        self.assertTrue(Matrix([]).approx_equal(Matrix([])))

    def test_approx_tol_zero(self):
        a = Matrix([[1.0]])
        b = Matrix([[1.0]])
        self.assertTrue(a.approx_equal(b, tol=0.0))


if __name__ == '__main__':
    unittest.main()
