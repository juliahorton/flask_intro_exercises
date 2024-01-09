""" 
A simple calculator built with Flask that uses URL query parameters to retrieve the operands.

Responds to 4 different routes, each of which performs a particular math operation on two numbers, a and b, which are passed in as URL GET-style query parameters.

Helper functions for mathematical operations located in operations.py.

Arguments 
---------------
a: first operand
b: second operand

Routes
---------------
/add
    Adds a and b and returns result in HTML document body
/sub
    Same, subtracting b from a
/mult 
    Same, multiplying a and b
/div
    Same, dividing a by b
"""

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def add_nums():
    a = int(request.args["a"])
    b = int(request.args["b"])
    sum = add(a,b)
    return str(sum)

@app.route("/sub")
def sub_nums():
    a = int(request.args["a"])
    b = int(request.args["b"])
    difference = sub(a,b)
    return str(difference)

@app.route("/mult")
def mult_nums():
    a = int(request.args["a"])
    b = int(request.args["b"])
    product = mult(a,b)
    return str(product)

@app.route("/div")
def div_nums():
    a = int(request.args["a"])
    b = int(request.args["b"])
    quotient = div(a,b)
    return str(quotient)

@app.route("/math/<operation>")
def do_math(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    
    math_funcs = {
    "add": add(a,b),
    "sub": sub(a,b),
    "mult": mult(a,b),
    "div": div(a,b)
    }

    return str(math_funcs[operation])
