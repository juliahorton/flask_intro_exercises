"""
A simple Flask app that responds to the following requests with the specified text messages:

/welcome (returns "Welcome")
/welcome/home (returns "Welcome home")
/welcome/back (returns "Welcome back")
"""

from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def say_welcome():
    """Return simple "Welcome" greeting"""
    return "Welcome"

@app.route("/welcome/home")
def say_welcome_home():
    """Return simple "Welcome home" greeting"""
    return "Welcome home"

@app.route("/welcome/back")
def say_welcome_back():
    """Return simple "Welcome back" greeting"""
    return "Welcome back"