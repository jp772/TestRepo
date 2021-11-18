"""Calculation history Class"""
class Calculations:
    """This is calculatios class whcih will perform all below functions"""
    history = []
    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """Clear history method"""
        Calculations.history.clear()
        return True
    @staticmethod
    def count_history():
        """History Count method"""
        return len(Calculations.history)
    @staticmethod
    def get_last_calculation():
        """Get the last calculation"""
        return Calculations.history[-1]
    @staticmethod
    def get_first_calculation():
        """Get the last calculation"""
        return Calculations.history[-1]
    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]
    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation)
