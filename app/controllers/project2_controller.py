from app.controllers.controller import ControllerBase
from flask import render_template, flash

class Page1(ControllerBase):
    """Class will get Page 1 which is Pylint Tutorial"""
    @staticmethod
    def get():
        return render_template('Pylint&OOPTutorial.html')

class Page2(ControllerBase):
    """Class will get Page 2 which is OOP Tutorial"""
    @staticmethod
    def get():
        return render_template('OOPProgramming.html')

class Page3(ControllerBase):
    """Class will get Page 3 which is AAA Tutorial"""
    @staticmethod
    def get():
        return render_template('AAATesting.html')

class Page4(ControllerBase):
    """Class will get Page 4 which is SOLID Tutorial"""
    @staticmethod
    def get():
        return render_template('SOLIDTesting.html')




