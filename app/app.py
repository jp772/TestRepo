"""A simple flask web app"""

from flask import Flask, flash, render_template
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.project2_controller import Page1, Page2, Page3, Page4
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

#pylint : disable=import-error
#pylint : disable=no-name-in-module
#pylint : disable=unused-import

@app.route("/", methods=['GET'])
def index_get():
    """fetches the get method from IndexController"""
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    """fetches the get method from IndexController"""
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    """fetches the get method from IndexController"""
    return CalculatorController.post()

@app.route("/PylintTutorial", methods=["GET"])
def page1_get():
    """fetches page 1 from Project2_controller"""
    return Page1.get()

@app.route("/OOPTutorial", methods=["GET"])
def page2_get():
    """fetches page 2 from Project2_controller"""
    return Page2.get()

@app.route("/AAATutorial", methods=["GET"])
def page3_get():
    """fetches page 3 from Project2_controller"""
    return Page3.get()

@app.route("/SOLIDTutorial", methods=["GET"])
def page4_get():
    """fetches page 4 from Project2_controller"""
    return Page4.get()
