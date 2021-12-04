"""Testing Multiplication"""
from calc.calculations.multiplication import Multiplication
import pandas as pd

def test_calculation_multiplication():
    """testing that our calculator has a static method for addition"""
    df = pd.read_csv("csvfiles/multiplication.csv")
    print(df.head(5))
    for i, j in df.iterrows():
        multi = (j.col1, j.col2)
        multiplication = Multiplication.create(multi)
        assert multiplication.get_result() == df['result'][i]
