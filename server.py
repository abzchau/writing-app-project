"""Server for writing app."""

"""Import flask module. An instance of this class will be our WSGI application."""
from flask import Flask, render_template, request, redirect
import model
import crud

"""Creates an instance of the Flask class."""
app = Flask(__name__)

"""The decorator tells Flask what URL should trigger our function. For example, when the homepage is opened in the browser, the output of this function will be rendered"""
@app.route('/')
def homepage():
    return "Bah"

""""Flask method which runs the app"""
if __name__ == '__main__':
    app.run(debug = True)
