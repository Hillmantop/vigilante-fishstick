import os

from flask import Flask, render_template, request

# this version of the app is to see what is happening in the layout.html it is not final
# in anyway

# Configure application
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("layout.html")


