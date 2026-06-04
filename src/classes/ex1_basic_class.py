"""
Exercise 1 — Basic classes: Rectangle

Tasks:
- Implement the Rectangle class: __init__, area, perimeter, scale, __str__
- Pay attention to argument validation (width and height must be positive numbers)

Instructions:
- Where indicated, replace the placeholder by implementing the method body. The placeholder is a single line: raise NotImplemented
- Each method you implement must include the documented behavior described in its docstring.

Run tests by executing this file: python src/ex1_basic_class.py
"""

import math
import unittest

class Rectangle:
    """A simple rectangle.

    Attributes:
        width (float): width of the rectangle (> 0)
        height (float): height of the rectangle (> 0)
    """

    def __init__(self, width: float, height: float):
        """Create a Rectangle.

        Args:
            width (float): positive width
            height (float): positive height

        Raises:
            ValueError: if width or height are not positive numbers
        """
        raise NotImplemented

    def area(self) -> float:
        """Return the area (width * height)."""
        raise NotImplemented

    def perimeter(self) -> float:
        """Return the perimeter (2*(width + height))."""
        raise NotImplemented

    def scale(self, factor: float):
        """Scale both width and height by factor.

        Args:
            factor (float): multiplier; must be positive

        Raises:
            ValueError: if factor is not positive
        """
        raise NotImplemented

    def __str__(self) -> str:
        """Return a readable representation: Rectangle(width=..., height=...)

        This should use floating point values with no extra rounding.
        """
        raise NotImplemented


# -------------------- Tests --------------------
class TestRectangle(unittest.TestCase):
    def test_area_perimeter(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)
        self.assertEqual(r.perimeter(), 14)

    def test_scale(self):
        r = Rectangle(2, 5)
        r.scale(2)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 10)

    def test_invalid_init(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 1)
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)

    def test_invalid_scale(self):
        r = Rectangle(1,1)
        with self.assertRaises(ValueError):
            r.scale(0)

    def test_str(self):
        r = Rectangle(1.5, 2.0)
        s = str(r)
        self.assertIn('Rectangle', s)
        self.assertIn('width=1.5', s)
        self.assertIn('height=2.0', s)


if __name__ == '__main__':
    unittest.main()
