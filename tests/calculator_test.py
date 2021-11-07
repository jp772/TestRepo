"""Testing the Calculator_main"""
from calculator.main import Calculator

def test_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_add():
    """Testing the Add function of the calculator"""
    #Calls the calculator class from main.py
    calc = Calculator()
    #Calls the add function from main.py and inputs static number.
    calc.add_number(8)
    #Assert that the results are correct
    assert calc.result == 8

def test_get_result():
    """Calls the calculator class from main.py"""
    calc = Calculator()
    # Assert that the results are correct
    assert calc.get_result() == 0

def test_subtract():
    """Calls the calculator class from main.py"""
    calc = Calculator()
    # Calls the subtract function from main.py and inputs static number.
    calc.subtract_number(2)
    # Assert that the results are correct
    assert calc.get_result() == -2
def test_multiply():
    """Calls the calculator class from main.py"""
    calc = Calculator()
    # Calls the multiplication function from main.py and inputs static number.
    result  = calc.multiply_numbers(2,2)
    # Assert that the results are correct
    assert result == 4
def test_divison():
    """Calls the calculator class from main.py"""
    calc = Calculator()
    # Calls the division function from main.py and inputs static number.
    result = calc.division_number(6,3)
    # Assert that the results are correct
    assert result == 2
