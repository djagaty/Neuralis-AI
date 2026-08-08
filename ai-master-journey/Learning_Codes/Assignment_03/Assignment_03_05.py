from abc import ABC, abstractmethod
import math


class Shape(ABC):
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
    try:
        Shape()
        assert False, "expected TypeError instantiating abstract class"
    except TypeError:
        pass

    c = Circle(3)
    assert abs(c.calculate_area() - math.pi * 9) < 1e-9
    assert isinstance(c, Shape)

    c0 = Circle(0)
    assert c0.calculate_area() == 0

    try:
        Circle(-2)
        assert False, "expected ValueError for negative radius"
    except ValueError:
        pass

    r = Rectangle(4, 5)
    assert r.calculate_area() == 20
    assert isinstance(r, Shape)

    r0 = Rectangle(0, 5)
    assert r0.calculate_area() == 0

    try:
        Rectangle(-1, 5)
        assert False, "expected ValueError for negative width"
    except ValueError:
        pass

    print("all tests passed")
