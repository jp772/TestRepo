"""Testing Subtraction"""
from calc.calculations.subtraction import Subtraction
import pandas as pd

def test_calculation_subtraction():
    """testing addition calculation from csv input"""
    df = pd.read_csv("csvfiles/subtraction.csv")
    print(df.head(5))
    for i, j in df.iterrows():
        sub = (j.col1, j.col2)
        subtraction = Subtraction.create(sub)
        assert subtraction.get_result() == df['result'][i]