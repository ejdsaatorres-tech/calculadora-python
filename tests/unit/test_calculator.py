import pytest
from src.calculator import add, subtract, divide

#prueba suma
def test_add():
    assert add(2, 3) == 5

#prueba resta
def test_subtract():
    assert subtract(5, 3) == 2
#prueba division
def test_divide():
    assert divide(10, 2) == 5

#prueba excepcion
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)