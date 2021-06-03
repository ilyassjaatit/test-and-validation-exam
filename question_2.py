"""
Question 2:
    Implement the following design pattern Factory:
"""
import abc


class ShapeBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self):
        pass


class Circle(ShapeBase):
    def draw(self):
        return "Circle"


class Square(ShapeBase):
    def draw(self):
        return "Square"


class Rectangle(ShapeBase):
    def draw(self):
        return "Rectangle"


def shape_factory(shape="square"):
    shapes = {"square": Square, "circle": Circle, "rectangle": Rectangle}
    return shapes[shape]()
