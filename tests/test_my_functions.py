import pytest
import source.my_functions as my_functions


def test_add():
    assert my_functions.add(1, 2) == 3
    assert my_functions.add(0, 0) == 0
    assert my_functions.add(-1, 1) == 0
    assert my_functions.add(-1, -1) == -2
    assert my_functions.add(1, -1) == 0

