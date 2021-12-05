"""Testing Subtraction"""
import time
import logging
import os
import pandas as pd
from calc import log
from calc.calculations.subtraction import Subtraction

def test_calculation_subtraction():
    """testing addition calculation from csv input"""
    filename = 'subtraction.csv'
    df = pd.read_csv("Input Files/subtraction.csv")
    print(df.head(5))
    for i, j in df.iterrows():
        sub = (j.col1, j.col2)
        record_num = i
        subtraction = Subtraction.create(sub)
        log.log_data_to_logfile(time, record_num, filename, j.col1, " + ", j.col2, df["result"][i])
        assert subtraction.get_result() == df["result"][i]