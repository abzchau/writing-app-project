"""Server for writing app."""

"""Import flask module. An instance of this class will be our WSGI application."""
from flask import Flask, render_template, request, redirect, session, flash, redirect
from model import connect_to_db
import crud
from jinja2 import StrictUndefined


"""Creates an instance of the Flask class."""
app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


"""The decorator tells Flask what URL should trigger our function. For example, when the homepage is opened in the browser, the output of this function will be rendered"""
@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/login', methods=["GET"])
def show_login():
    return "Sign In"


@app.route('/login', methods=["POST"])
def process_login():
    return "Use Form Data To Sign In User"


@app.route('/signup')
def show_sign_up():
    return render_template("signup.html")


@app.route('/signup', methods=["POST"])
def process_sign_up():
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("password")
    repeatPassword = request.form.get("repeatPassword")
    
    print(fname, lname, email, password)
    return render_template("signup.html")


@app.route('/signed_up')
def show_signed_up_page():
    return "You are signed up. Add a link here."


@app.route('/about')
def about_the_app():
    return "About the app"


""""Flask method which runs the app"""
if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug = True)
