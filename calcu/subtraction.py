"""This is the addition calculation which is being inherits the
value A and B from calculation class"""

from calcu.calculation import Calculation

#This is how you extened the addition class with caclulation
class Subtraction(Calculation):
    """This addition class has one method to get the result of the
    calculation A and B from the calcualtion parent class"""
    def get_result(self):
        """Get Result is returning the self.value A and B"""
        #your you need to use self to reference the data contained in the
        # instance of the object. this is encapsulation
        return self.value_a - self.value_b
