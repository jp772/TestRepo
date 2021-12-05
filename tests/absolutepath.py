import pandas as pd
from pathlib import Path

class csv_manager:

    def get_data_frame_from_csv(filename):
        return pd.read_csv(file_utilities.absolutepath(filename))


class file_utilities:
    @staticmethod
    def absolutepath(filepath):
        relative = Path(filepath)
        return relative.absolute()