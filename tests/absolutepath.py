import pandas as pd
from pathlib import Path

def absolutepath(filepath):
    relative = Path(filepath)
    return relative.absolute()