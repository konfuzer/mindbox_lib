import math
from .base import Shape

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
        self._validate_triangle()

    def _validate_triangle(self):
        # Проверка на возможность существования треугольника
        if (self.a + self.b <= self.c or
            self.a + self.c <= self.b or
            self.b + self.c <= self.a):
            raise ValueError("Invalid triangle sides")

    def area(self) -> float:
        # Формула Герона
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_triangle(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2, rel_tol=1e-9)
