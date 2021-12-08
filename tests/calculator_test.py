"""Importing pytest for the static fixture"""

import pytest
import os
import pandas as pd
from calc.history.calculations import Calculations
from calc.calculations.addition import Addition
from calc.calculations.multiplication import Multiplication
from calc.calculations.subtraction import Subtraction
from calc.calculations.division import Division

dirname = os.path.dirname("addition.csv")

@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()
#You have to add the fixture function as a parameter to the test that you want to use it with
def test_calculator_add_static(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    #using Tuple instead of args because we can pack as much data as we need into the tuple

    filename = os.path.join(dirname, 'Input Files/addition.csv')
    df = pd.read_csv(filename)
    print(df.head(5))
    for i, j in df.iterrows():
        sum = (j.col1, j.col2)
        addition = Addition.create(sum)
        logger.error("Input Files")
        assert addition.get_result() == df['result'][i]

def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    #using Tuple instead of args because we can pack as much data as we need into the tuple
    dirname = os.path.dirname("subtraction.csv")
    filename = os.path.join(dirname, 'Input Files/subtraction.csv')
    df = pd.read_csv(filename)
    print(df.head(5))
    for i, j in df.iterrows():
        sub = (j.col1, j.col2)
        subtraction = Subtraction.create(sub)
        assert subtraction.get_result() == df['result'][i]

def test_calculator_multiply_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    #using Tuple instead of args because we can pack as much data as we need into the tuple
    dirname = os.path.dirname("multiplication.csv")
    filename = os.path.join(dirname, 'Input Files/multiplication.csv')
    df = pd.read_csv(filename)
    print(df.head(5))
    for i, j in df.iterrows():
        multi = (j.col1, j.col2)
        multiplication = Multiplication.create(multi)
        assert multiplication.get_result() == df['result'][i]

def test_calculator_divide_static(clear_history_fixture):
    dirname = os.path.dirname("division.csv")
    filename = os.path.join(dirname, 'Input Files/division.csv')
    df = pd.read_csv(filename)
    print(df.head(5))
    for i, j in df.iterrows():
        div = (j.col1, j.col2)
        division = Division.create(div)
        try:
            assert division.get_result() == df['result'][i]
        except ZeroDivisionError:
            print("Zero Division Error occurred")