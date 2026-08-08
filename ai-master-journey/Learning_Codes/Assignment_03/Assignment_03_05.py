from abc import ABC, abstractmethod
import math


class Shape(ABC):
    # abstractmethod forces every subclass to provide its own calculate_area
    # Shape itself can never be instantiated directly
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("radius cannot be negative")
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("width and height cannot be negative")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


if __name__ == "__main__":
    import os

    # sample inputs that answer the exercise
    circle = Circle(3)
    rectangle = Rectangle(4, 5)
    lines = [
        f"Circle area: {circle.calculate_area():.4f}",
        f"Rectangle area: {rectangle.calculate_area()}",
    ]

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assignment_03_05_output.txt")
    with open(output_path, "w") as f:
        f.write("\n".join(lines) + "\n")
    for line in lines:
        print(line)

    # edge and negative case checks
    try:
        Shape()
        assert False, "expected TypeError instantiating abstract class"
    except TypeError:
        pass

    assert abs(circle.calculate_area() - math.pi * 9) < 1e-9
    assert isinstance(circle, Shape)

    circle_zero = Circle(0)
    assert circle_zero.calculate_area() == 0

    try:
        Circle(-2)
        assert False, "expected ValueError for negative radius"
    except ValueError:
        pass

    assert rectangle.calculate_area() == 20
    assert isinstance(rectangle, Shape)

    rectangle_zero = Rectangle(0, 5)
    assert rectangle_zero.calculate_area() == 0

    try:
        Rectangle(-1, 5)
        assert False, "expected ValueError for negative width"
    except ValueError:
        pass

    print("all tests passed")
