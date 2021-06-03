from question_2 import shape_factory, Circle, Square, Rectangle


def test_shape_factory():
    circle = shape_factory("circle")
    assert isinstance(circle, Circle)


def test_shape_square_draw():
    square = shape_factory("square")
    assert isinstance(square, Square)
    assert square.draw() == "Square"


def test_shape_circle_draw():
    circle = shape_factory("circle")
    assert isinstance(circle, Circle)
    assert circle.draw() == "Circle"


def test_shape_rectangle_draw():
    rectangle = shape_factory("rectangle")
    assert isinstance(rectangle, Rectangle)
    assert rectangle.draw() == "Rectangle"
