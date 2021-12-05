"""Testing Multiplication"""
import time
import logging
import pandas as pd
from calc import log
from calc.calculations.multiplication import Multiplication

def test_calculation_multiplication():
    """testing that our calculator has a static method for multiplication"""
    filename = 'multiplication.csv'
    df = pd.read_csv("Input Files/multiplication.csv")
    print(df.head(5))
    for i, j in df.iterrows():
        multi = (j.col1, j.col2)
        record_num = i
        multiplication = Multiplication.create(multi)
        log.log_data_to_logfile(time, record_num, filename, j.col1, " * ", j.col2, df["result"][i])
        assert multiplication.get_result() == df["result"][i]
