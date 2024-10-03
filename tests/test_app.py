import pytest
from app.app import Calculator

# Initialize the calculator
calc = Calculator()

def test_addition():
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_subtraction():
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(5, 10) == -5

def test_multiplication():
    assert calc.multiply(4, 5) == 20
    assert calc.multiply(-1, 5) == -5

def test_division():
    assert calc.divide(10, 2) == 5
    with pytest.raises(ValueError):
        calc.divide(10, 0)  # This should raise an error for division by zero

def test_invalid_inputs():
    with pytest.raises(TypeError):
        calc.add("a", 3)  # Expecting a TypeError because "a" is not a number
