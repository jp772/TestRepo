""" This is the increment function"""
class Calculator:
    """ This is the Calculator class"""
    result = 0
    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def add_number(self, sum_a):
        """ adds number to result"""
        self.result = self.result + sum_a
        return self.result
    def subtract_number(self, sub_a):
        """ subtract number from result"""
        self.result = self.result - sub_a
        return self.result
    def multiply_numbers(self, mul_1, mul_2):
        """ multiply two numbers and store the result"""
        self.result = mul_1 * mul_2
        return self.result
    def division_number(self, div_1, div_2):
        """ Divide two numbers and store the result"""
        self.result = div_1 / div_2
        return self.result
