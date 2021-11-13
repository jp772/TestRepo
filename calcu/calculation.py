"""This is our calculation base class"""
class Calculation:
    """Constructor class"""
    def __init__(self, value_a, value_b):
        """This allows the class to initialize the attributes of the class"""
        self.value_a = value_a
        self.value_b = value_b
    @classmethod
    def create(cls, value_a, value_b):
        """This is for creating itself as an object"""
        return cls(value_a, value_b)
