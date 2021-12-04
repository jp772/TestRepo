"""Multiplication Class"""
from calc.calculations.calculation import Calculation

class Multiplication(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the multiplication results"""
        multi1 = enumerate(self.values)
        for i, value in (multi1):
            if i != 0:
                result = result * value
            else:
                result = value
        return result