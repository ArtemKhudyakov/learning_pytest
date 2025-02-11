import pytest
import src.culc as culc


# Тест функции сложения
def test_add():
    assert culc.add(2, 3) == 5
    assert culc.add(-2, 3) == 1
    assert culc.add(0, 0) == 0

# Тест функции вычитания
def test_subtract():
    assert culc.subtract(2, 3) == -1
    assert culc.subtract(-2, 3) == -5
    assert culc.subtract(0, 0) == 0

# Тест функции умножения
def test_multiply():
    assert culc.multiply(2, 3) == 6
    assert culc.multiply(-2, 3) == -6
    assert culc.multiply(0, 0) == 0

# Тест функции деления
def test_divide():
    assert culc.divide(6, 2) == 3
    assert culc.divide(-6, 3) == -2
    assert culc.divide(0, 5) == 0
    with pytest.raises(ZeroDivisionError):
        culc.divide(6, 0)