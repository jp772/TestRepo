""" This is the increment function"""

from calcu.addition import Addition
from calcu.subtraction import Subtraction
from calcu.multiplication import Multiplication
from calcu.division import Division

class Calculator:
    """ This is the Calculator class"""
    history = []

    @staticmethod
    def clear_history():
        """This method clears the history"""
        Calculator.history.clear()
        return True

    @staticmethod
    def history_count():
        """This method counts the calculations"""
        return len(Calculator.history)

    @staticmethod
    def add_calculation_to_history(calculation):
        """This method adds all the result to calculation"""
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        """this object add the last item to history and will get the results automatically."""
        return Calculator.history[0].get_result()

    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        """this object add the last item to history and will get the results automatically."""
        return Calculator.history[-1].get_result()

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        #create an addition object
        addition = Addition.create(value_a, value_b)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        subtraction = Subtraction.create(value_a, value_b)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and store the result"""
        multiplication = Multiplication.create(value_a, value_b)
        Calculator.add_calculation_to_history(multiplication)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def division_number(value_a, value_b):
        """ Divide two numbers and store the result"""
        division = Division.create(value_a, value_b)
        Calculator.add_calculation_to_history(division)
        return Calculator.get_result_of_last_calculation_added_to_history()
