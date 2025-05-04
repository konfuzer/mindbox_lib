import unittest
from mindbox_lib.circle import Circle
from mindbox_lib.triangle import Triangle
from mindbox_lib.shapes import AreaCalculator
import math

class TestShapes(unittest.TestCase):
    def setUp(self):
        self.calc = AreaCalculator()

    def test_circle_area(self):
        circle = Circle(10)
        self.assertAlmostEqual(self.calc.calculate(circle), math.pi * 100, places=5)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(self.calc.calculate(triangle), 6.0, places=5)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

    def test_non_right_triangle(self):
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right_triangle())

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)

if __name__ == '__main__':
    unittest.main()
