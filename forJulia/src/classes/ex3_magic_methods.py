"""
Exercise 3 — Magic methods and immutability

Tasks:
- Implement a small 2D vector class Vector2D that behaves like a value object.
- Implement __init__, __eq__, __repr__, __add__, __neg__, __mul__ (scalar multiply), and magnitude property

Notes:
- Vector2D instances should be immutable: once created, x and y should not be settable.
- Equality compares numeric equality of coordinates.

Run tests: python src/ex3_magic_methods.py
"""
import math
import unittest

class Vector2D:
    """2D vector value object.

    Attributes:
        x (float): x-coordinate
        y (float): y-coordinate
    """

    def __init__(self, x: float, y: float):
        """Initialize coordinates (floats)."""
        raise NotImplemented

    @property
    def magnitude(self) -> float:
        """Return the Euclidean norm sqrt(x*x + y*y)."""
        raise NotImplemented

    def __eq__(self, other) -> bool:
        """Compare vectors by coordinates. Return NotImplemented for unsupported types."""
        raise NotImplemented

    def __repr__(self) -> str:
        """Return a constructor-like representation: Vector2D(x, y)"""
        raise NotImplemented

    def __add__(self, other):
        """Add two vectors coordinate-wise; return a new Vector2D."""
        raise NotImplemented

    def __neg__(self):
        """Return a new Vector2D that is the negation of this vector."""
        raise NotImplemented

    def __mul__(self, scalar: float):
        """Multiply by a scalar (from right). Return a new Vector2D."""
        raise NotImplemented


# -------------------- Tests --------------------
class TestVector2D(unittest.TestCase):
    def test_repr_and_eq(self):
        v1 = Vector2D(1, 2)
        v2 = Vector2D(1.0, 2.0)
        self.assertEqual(v1, v2)
        self.assertIn('Vector2D', repr(v1))

    def test_add_and_neg(self):
        a = Vector2D(1, 1)
        b = Vector2D(2, -3)
        c = a + b
        self.assertEqual(c, Vector2D(3, -2))
        self.assertEqual(-a, Vector2D(-1, -1))

    def test_mul_and_magnitude(self):
        v = Vector2D(3, 4)
        self.assertEqual(v.magnitude, 5)
        self.assertEqual(v * 2, Vector2D(6, 8))

    def test_immutable(self):
        v = Vector2D(0, 0)
        with self.assertRaises(AttributeError):
            v.x = 10


if __name__ == '__main__':
    unittest.main()
