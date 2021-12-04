"""Testing Addition"""
import os
import logging
from calc.calculations.addition import Addition
from calculator.main import Calculator
import pandas as pd

def test_calculation_addition():
    """testing addition calculation from csv input"""
    df = pd.read_csv("csvfiles/addition.csv")
    print(df.head(5))
    for i, j in df.iterrows():
        sum = (j.col1, j.col2)
        addition = Addition.create(sum)
        assert addition.get_result() == df['result'][i]




