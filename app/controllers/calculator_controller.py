from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for
from calc.history.calculations import Calculations

class CalculatorController(ControllerBase):
    """This class will prompt user if there is no values provided and if there is, it will do the operation accordingly"""
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'Please enter value 1 and value 2'

        else:
            flash('You successfully calculated')
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            #Open file and write to it.
            file = open("result.csv","a")
            file.write(f'Operation: {operation}, Values1: {value1}, Value2: {value2}, Results= {result}\n\n')
            file.close()
            #return results page with values and results
            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result)
        return render_template('calculator2.html', error=error)
    @staticmethod
    def get():
        return render_template('calculator2.html')