"""Server for writing app."""

"""Import flask module. An instance of this class will be our WSGI application."""
from flask import Flask, render_template, request, redirect, session, flash, redirect, url_for
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
    """View Homepage"""
    return render_template("homepage.html")


@app.route('/login', methods=["POST", 'GET'])
def login():
    """Process log in information"""

    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = crud.get_user_by_email(email)

        if not user or user.password != password:
            flash("The email or password you entered is incorrect. Try again.")
            return render_template("/login.html")
        else:
            session["user_email"] = user.email
            session["user_id"] = user.user_id
            flash(f"Welcome back, {user.email}!")
            return redirect(url_for("main"))
    else:
        return render_template('/login.html')


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Sign up a new user"""
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("password")
    favorite_writer = request.form.get("favorite_writer")
    favorite_animal = request.form.get("favorite_animal")
    user = crud.get_user_by_email(email)
    if request.method == 'POST':
        if user:
            flash('It looks like you already have an account. Try to log in with your email and password.')
            return render_template('signup.html')
        else:
            crud.create_user(fname, lname, email, password, favorite_writer, favorite_animal)
            flash("'We've created your account. Please log in.")
            return render_template('/login.html')
    else:
        return render_template("signup.html")


@app.route('/main', methods=["GET", "POST"])
def main():
    """Create a group or project"""
    
    if request.method == 'POST':
        if "group_name" in request.form:
            group_name = request.form.get("group_name")
            group = crud.create_group(group_name)
            user_id = session["user_id"]
            print(user_id)
            user = crud.get_user_by_id(user_id)
            crud.create_association(group, user)
            session["group_id"] = group.group_id
            session["group_name"] = group.group_name
            flash('Group Created')
            return redirect(f"/group/{group_name}")
        
        if "project_name" in request.form:
            user_id = session["user_id"]
            group_id = 1
            project_name = request.form.get("project_name")
            genre = request.form.get("genre")
            project = crud.create_project(project_name, user_id, genre)
            session["project_name"] = project_name
            session["project_id"] = project.project_id
            flash('Project Created')
            return redirect(f"/project/{project_name}")
    else:
        group_name = request.form.get("group_name")
        return render_template("/main.html", group_name=group_name)


@app.route('/group/<group_name>')
def group_homepage(group_name):
    group_name = session["group_name"]
    return render_template('/group.html', group_name=group_name)


@app.route('/project/<project_name>')
def project_homepage(project_name):
    project_name = session["project_name"]
    print(project_name)
    return render_template('/project.html', project_name=project_name)

@app.route('/group', methods=["POST"])
def add_user_to_group():
    """Add another user to a group"""
    email = request.form.get("email")
    user = crud.get_user_by_email(email)
    group_name = session["group_name"]
    print(session["group_name"])

    if not user:
        flash("The user does not exist. Please try again, or have the user sign up.")
        return render_template("/group.html", group_name=group_name)
    else:
        email = request.form.get("email")
        user = crud.get_user_by_email(email)
        group_id = session["group_id"]
        group = crud.get_group_by_id(group_id)
        crud.create_association(group, user)
            
        return render_template("/group.html", group_name=group_name)


@app.route('/project', methods=["POST"])
def add_group_to_project():
    project_id = session["project_id"] 
    print(project_id)
    group_name = request.form.get("group_name")
    print(group_name)
    group_id = crud.get_group_id_by_name(group_name)
    print(group_id)
    crud.add_group_to_project(group_id, project_id)
    return render_template('/project.html')


@app.route('/project_page')
def project_page():
    return render_template('project_page.html')



@app.route('/about')
def about_the_app():
    return "About the app"


""""Flask method which runs the app"""
if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug = True, host='0.0.0.0')