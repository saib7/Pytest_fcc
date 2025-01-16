import pytest


def test_area(my_rectangle):
    assert my_rectangle.area() == 5*10

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 2 * (5 + 10)

def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle
