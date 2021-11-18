"""Testing Division"""
from calc.calculations.division import Division

def test_calculation_division():
    """testing that our calculator has a static method for addition"""
    #Arrange
    nums = (3.0,6.0)
    division = Division(nums)
    #Act
    #Assert
    assert division.get_result() == 2
