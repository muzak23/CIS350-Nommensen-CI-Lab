from math_functions import Calculator

def test_calc_addition():
    output = Calculator.add_numbers(2,4)
    assert output == 6
def test_calc_substraction():
    output = Calculator.subtract_numbers(2, 4)
    assert output == -2
def test_calc_multiply():
    output = Calculator.multiply_numbers(2,4)
    assert output == 8
def test_calc_multiply_fail():
    output = Calculator.multiply_numbers(4,4)
    assert output == 16
def test_calc_divide():
    output = Calculator.divide_numbers(10,2)
    assert output == 5
def test_calc_opposite():
    output = Calculator.opposite(2)
    assert output == -2
def test_calc_modulo():
    output = Calculator.modulo(2, 4)
    assert output == 2
