"""A simple flask web app"""
from flask import Flask
from flask import flash, render_template
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.project2_controller import Page1
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

#pylint : disable=import-error
#pylint : disable=no-name-in-module
#pylint : disable=unused-import

@app.route("/", methods=['GET'])
def index_get():
    flash("Testing Flash")
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/PylintTutorial", methods=["GET"])
def page1_get():
    """Page 1 route"""
    return Page1.get()

@app.route("/OOPTutorial", methods=["GET"])
def page1_get():
    """Page 1 route"""
    return Page1.get()

@app.route("/AAATutorial", methods=["GET"])
def page1_get():
    """Page 1 route"""
    return Page1.get()

@app.route("/SOLIDTutorial", methods=["GET"])
def page1_get():
    """Page 1 route"""
    return Page1.get()
