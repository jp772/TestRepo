"""Testing Division"""
import time
import logging
import pandas as pd
from calc import log
from calc.calculations.division import Division

#excep_logs = pd.read_csv("../tests/Results_Log/Exceptionfile.log")

def test_calculation_division():
    """testing that our calculator has a static method for division"""
    filename = 'division.csv'
    df = pd.read_csv("Input Files/division.csv")
    print(df.head(5))
    for i, j in df.iterrows():
        div = (j.col1, j.col2)
        record_num = i
        division = Division.create(div)

        try:
            log.log_data_to_logfile(time, record_num, filename, j.col1, " / ", j.col2, df["result"][i])
            assert division.get_result() == df['result'][i]
        except ZeroDivisionError as message:
            #excep_logs.to_csv("../tests/Results_Log/Exceptionfile.log")
            log.logger.error("Zero Division Error occurred, Cannot Divide Number By 0")
            assert division.get_result() is True
            continue




