""" This is the increment function"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division
from calc.history.calculations import Calculations

class Calculator:
    """ This is the Calculator class"""
    @staticmethod
    def add_number(*args):
        """ adds number to result"""
        calculation = Addition(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
    @staticmethod
    def subtract_number(*args):
        """ subtract number from result"""
        calculation = Subtraction(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
    @staticmethod
    def multiply_number(*args):
        """ multiply two numbers and store the result"""
        calculation = Multiplication(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
    @staticmethod
    def division_number(*args):
        """ Divide two numbers and store the result"""
        calculation = Division(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
