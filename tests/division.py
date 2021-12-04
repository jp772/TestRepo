"""Testing Division"""
from calc.calculations.division import Division
import pandas as pd

def test_calculation_division():
    """testing that our calculator has a static method for addition"""
    df = pd.read_csv("csvfiles/division.csv")
    print(df.head(5))
    for i, j in df.iterrows():
        div = (j.col1, j.col2)
        division = Division.create(div)
        try:
            assert division.get_result() == df['result'][i]
        except ZeroDivisionError:
            print ("Zero Division Error occurred")


