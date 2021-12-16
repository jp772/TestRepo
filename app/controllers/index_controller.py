from app.controllers.controller import ControllerBase
from flask import render_template, flash

class IndexController(ControllerBase):
    """This class returns the index page."""
    @staticmethod
    def get():
        return render_template('index.html')
