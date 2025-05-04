# midbox_lib

# mindbox_lib

📐 Простая и расширяемая Python-библиотека для вычисления площади геометрических фигур.  
Поддерживаются: круги, треугольники (в том числе проверка на прямоугольность).

---

## 🔧 Установка

Установка из локального источника:

    ```bash
    git clone https://github.com/yourusername/mindbox_lib.git
    cd mindbox_lib
    pip install -e .

*🐍Использование*
    from mindbox_lib.shapes import AreaCalculator
    from mindbox_lib.circle import Circle
    from mindbox_lib.triangle import Triangle

    calculator = AreaCalculator()

    # Круг
    circle = Circle(radius=10)
    print("Площадь круга:", calculator.calculate(circle))  # 314.15...

    # Треугольник
    triangle = Triangle(3, 4, 5)
    print("Площадь треугольника:", calculator.calculate(triangle))  # 6.0
    print("Прямоугольный?", triangle.is_right_triangle())  # True

*✅ Тестирование*

Библиотека покрыта юнит-тестами (используется unittest из стандартной библиотеки).

Запуск:
    ```bash
    python -m unittest discover tests


*➕ Расширение*

Для добавления новой фигуры:

Создайте класс, унаследованный от Shape (из mindbox_lib/base.py).

Реализуйте метод area(self) -> float.

Готово! Объект этой фигуры будет поддерживаться AreaCalculator без изменений.

Пример:

from mindbox_lib.base import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


*🛠️ Требования*

Python 3.7+

**Разработано для тестового задания Mindbox.**