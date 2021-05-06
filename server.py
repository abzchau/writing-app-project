"""Server for writing app."""

"""Import flask module. An instance of this class will be our WSGI application."""
from flask import Flask, render_template, request, redirect, session, flash, redirect
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

from flask import Flask


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
    return render_template('/login.html')


@app.route('/login', methods=["POST"])
def process_login():

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if not user or user.password != password:
        flash("The email or password you entered is incorrect. Try again.")
        return redirect("/login")
    else:
        session["user_email"] = user.email
        session["user_id"] = user.user_id
        flash(f"Welcome back, {user.email}!")
        return render_template("/main.html")



@app.route('/signup')
def show_sign_up():
    return render_template("signup.html")


@app.route('/signup', methods=["GET", "POST"])
def register_user():
    "Create a new user"
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("password")
    favorite_writer = request.form.get("favorite_writer")
    favorite_animal = request.form.get("favorite_animal")
    user = crud.get_user_by_email(email)

    if user:
        flash('It looks like you already have an account. Try to log in with your email and password.')
        return render_template('signup.html')
    else:
        crud.create_user(fname, lname, email, password, favorite_writer, favorite_animal)
        flash("'We've created your account. Please log in.")
        return render_template('/login.html')

@app.route('/main')
def main():
    return render_template("/main.html")

@app.route('/main', methods=["POST"])
def create_group():

    group_name = request.form.get("group_name")
    group = crud.create_group(group_name)
    return render_template("/group.html", group_name=group_name)


@app.route('/group', methods=["POST"])
def create_project():

    if 'user_id' in session:
        user_id = session["user_id"]
        group_id = 1
        project_name = request.form.get("project_name")
        genre = request.form.get("genre")
    

        project = crud.create_project(project_name, user_id, group_id, genre)
        return render_template("/project.html", project_name=project_name, genre=genre)


@app.route('/group', methods=["POST"])
def add_user_to_group():
    
    print('yo hey')

    email = request.form.get("email")
    print(email)
    user = crud.get_user_by_email(email)
    print(user)
    user_group = crud.create_member(user.user_id, group_id)
    flash("Added to your group.")
        
    return render_template("/group.html")


@app.route('/about')
def about_the_app():
    return "About the app"


""""Flask method which runs the app"""
if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug = True, host='0.0.0.0')