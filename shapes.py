from .base import Shape

class AreaCalculator:
    def calculate(self, shape: Shape) -> float:
        return shape.area()
