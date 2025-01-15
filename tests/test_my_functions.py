import pytest
import source.my_functions as my_functions


def test_add():
    assert my_functions.add(1, 2) == 3
    assert my_functions.add(0, 0) == 0
    assert my_functions.add(-1, 1) == 0
    assert my_functions.add(-1, -1) == -2
    assert my_functions.add(1, -1) == 0


def test_add_string():
    assert my_functions.add("a", "b") == "ab"
    with pytest.raises(TypeError):
        my_functions.add("a", 1)
    with pytest.raises(TypeError):
        my_functions.add(1, "b")



def test_divide():
    assert my_functions.divide(1, 2) == 0.5
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(0, 0)
    assert my_functions.divide(-1, 1) == -1
    assert my_functions.divide(-1, -1) == 1
    assert my_functions.divide(1, -1) == -1

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(1, 0)
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(-1, 0)


