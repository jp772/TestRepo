"""Testing Division"""
import time, pytest
import logging
import pandas as pd
from calc import log
from calc.calculations.division import Division

#excep_logs = pd.read_csv("../tests/Results_Log/Exceptionfile.log")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
Log_Format = logging.Formatter('%(levelname)s %(asctime)s - %(message)s')
fh = logging.FileHandler('../tests/Results_Log/Exceptionfile.log')

fh.setFormatter(Log_Format)
logger.addHandler(fh)

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
            df_result = df['result'][i].round(decimals=5)
            log.log_data_to_logfile(time, record_num, filename, j.col1, " / ", j.col2, df_result)
            assert division.get_result() == df_result
        except ZeroDivisionError as message:
            #excep_logs.to_csv("../tests/Results_Log/Exceptionfile.log")
            logger.error("Zero Division Error occurred, Cannot Divide Number By 0")
            assert division.get_result() is True






