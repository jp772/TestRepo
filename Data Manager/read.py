import pandas as pd

class CsvReader:

    def get_dataframe_from_file(addition):
        """testing that our calculator has a static method for addition"""
        df = pd.read_csv("addition.csv")
        print(df)