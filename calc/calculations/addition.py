"""This is the addition calculation which is being
inherits the value A and B from calculation class"""

from calc.calculations.calculation import Calculation

#This is how you extened the addition class with caclulation
class Addition(Calculation):
    """This addition class has one method to get the result of the calculation
    A and B from the calcualtion parent class"""
    def get_result(self):
        """Get Result is returning the self.value A and B"""
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = value + sum_of_values
        return sum_of_values
