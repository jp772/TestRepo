"""Testing Addition"""
import time
import logging
import os
import pandas as pd
from calc import log
from calc.calculations.addition import Addition


def test_calculation_addition():
    """testing addition calculation from csv input"""
    filename = 'addition.csv'
    df = pd.read_csv("Input Files/addition.csv")
    print(df.head(5))
    for i, j in df.iterrows():
        sum = (j.col1, j.col2)
        record_num = i
        addition = Addition.create(sum)
        log.log_data_to_logfile(time, record_num, filename, j.col1, " + ", j.col2, df["result"][i])
        assert addition.get_result() == df["result"][i]




