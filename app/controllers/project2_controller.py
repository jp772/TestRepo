from app.controllers.controller import ControllerBase
from flask import render_template, flash

class Page1(ControllerBase):
    """page class"""
    @staticmethod
    def get():
        """getter method"""
        return render_template('../templates/Project2_pages/Pylint&OOPTutorial.html')

class Page2(ControllerBase):
    """page class"""
    @staticmethod
    def get():
        """getter method"""
        return render_template('../templates/Project2_pages/OOPProgramming.html')


