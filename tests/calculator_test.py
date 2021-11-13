"""Importing pytest for the static fixture"""
import pytest

from calculator.main import Calculator
@pytest.fixture()
def clear_history():
    """Testing clear history function"""
    Calculator.clear_history()

def test_addition(clear_history):
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 6

def test_clear_history(clear_history):
    """Testing clear history function"""
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.clear_history() == True
    assert Calculator.history_count() == 0

def test_count_history(clear_history):
    """Testing count history function"""
    assert Calculator.history_count() == 0
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.history_count() == 2

def test_get_last_calculation_result(clear_history):
    """Testing get last calculation function"""
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.get_result_of_last_calculation_added_to_history() == 3

def test_get_first_calculation_result(clear_history):
    """Testing get first calculation function"""
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.get_result_of_first_calculation_added_to_history() == 4

def test_subtract(clear_history):
    """Calls the calculator class from main.py"""
    assert Calculator.subtract_number(1,2) == -1

def test_multiply(clear_history):
    """Calls the calculator class from main.py"""
    assert Calculator.multiply_numbers(2,2) == 4

def test_divison(clear_history):
    """Calls the calculator class from main.py"""
    assert Calculator.division_number(6,3) == 2
