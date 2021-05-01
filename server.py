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


@app.route('/login', methods=["GET"])
def show_login():
    return "Sign In"


@app.route('/login', methods=["POST"])
def login_user():
    return "Use Form Data To Sign In User"


@app.route('/signup')
def show_sign_up():
    return "Sign Up"


@app.route('/signed_up')
def show_signed_up_page():
    return "You are signed up. Add a link here."


@app.route('/about')
def about_the_app():
    return "About the app"


""""Flask method which runs the app"""
if __name__ == '__main__':
    app.run(debug = True)
