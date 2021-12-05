"""This is the addition calculation which is being inherits the
value A and B from calculation class"""

from calc.calculations.calculation import Calculation

#This is how you extened the addition class with caclulation
class Division(Calculation):
    """This addition class has one method to get the result of the
    calculation A and B from the calcualtion parent class"""
    def get_result(self):
        """Get Result is returning the self.value A and B"""
        result = self.values[0] / self.values[1]
        return result
