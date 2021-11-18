"""This is the addition calculation which is being inherits the
value A and B from calculation class"""

from calc.calculations.calculation import Calculation

#This is how you extened the addition class with caclulation
class Multiplication(Calculation):
    """This addition class has one method to get the result of the
    calculation A and B from the calcualtion parent class"""
    def get_result(self):
        """get the multiplication results"""
        result = 1.0
        for value in self.values:
            result = result * value
        return result
