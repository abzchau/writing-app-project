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
    
    if request.method =="GET":
        return render_template('/login.html')

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
            return redirect(url_for("get_main"))

        


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Sign up a new user"""
    if request.method == 'GET':
        return render_template("signup.html")

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



@app.route('/main', methods=["GET"])
def get_main():
        """View the main page"""

        if 'user_id' in session:
            group_name = request.form.get("group_name")
            project_name = request.form.get("project_name")
            user_id = session["user_id"]
            lst_of_groups_by_user_id = crud.get_all_groups_by_user(user_id)
            lst_of_projects_by_user_id = crud.get_all_projects_by_user(user_id)
            return render_template("/main.html", group_name=group_name, lst_of_groups_by_user_id=lst_of_groups_by_user_id, project_name=project_name,lst_of_projects_by_user_id=lst_of_projects_by_user_id)


@app.route('/main', methods=["POST"])
def post_main():
    """Create a group or project on the main page"""
    
    if "group_name" in request.form:
        group_name = request.form.get("group_name")
        group = crud.create_group(group_name)
        session["group_id"] = group.group_id
        user_id = session["user_id"]
        user = crud.get_user_by_id(user_id)
        crud.create_association(group, user)
        flash('Group Created')
        return redirect(f"/group/{group_name}")
    
    if "project_name" in request.form:
        user_id = session["user_id"]
        project_name = request.form.get("project_name")
        genre = request.form.get("genre")
        project = crud.create_project(project_name, user_id, genre)
        flash('Project Created')
        return redirect(f"/project/{project_name}")


@app.route('/group/<group_name>')
def get_group(group_name):
    "Redirects Here After Creating a Group"

    if 'user_id' in session:
        group_id = crud.get_group_id_by_name(group_name)
        group = crud.get_group_by_id(group_id)
        lst_of_users_by_group = group.users
        return render_template('/group.html', group_name=group_name, lst_of_users_by_group=lst_of_users_by_group)


@app.route('/group', methods=["POST"])
def add_user_to_group():
    """Add another user to a group"""
    
    email = request.form.get("email")
    user = crud.get_user_by_email(email)
    group_name = request.form.get("group_name")

    if not user:
        flash("The user does not exist. Please try again, or have the user sign up.")
        return redirect(f"/group/{group_name}")
    else:
        email = request.form.get("email")
        user = crud.get_user_by_email(email)
        group_id = crud.get_group_id_by_name(group_name)
        group = crud.get_group_by_id(group_id)
        crud.create_association(group, user)
        lst_of_groups_by_user_id = crud.get_all_groups_by_user(user.user_id)
        lst_of_users_by_group = group.users
            
        return render_template("/group.html", group_name=group_name, lst_of_groups_by_user_id=lst_of_groups_by_user_id, lst_of_users_by_group=lst_of_users_by_group)


@app.route('/meeting_page', methods=["GET", "POST"])
def meeting_page():
    """View the Group's Meeting Page"""

    if 'user_id' in session:
        print('yoyomomo', 'user_id')
        group_name = request.form.get("group_name")
        group_id = crud.get_group_id_by_name(group_name)
        group = crud.get_group_by_id(group_id)
        lst_of_users_by_group = group.users

        #This section is to retrieve the text
        dict_of_users = crud.get_text_for_meeting_page(group_id)
        return render_template('/meeting_page.html', group_name=group_name, lst_of_users_by_group=lst_of_users_by_group, dict_of_users=dict_of_users)


@app.route('/project/<project_name>')
def get_project(project_name):
    """View Project Main Page"""
    
    project = crud.get_project_by_name(project_name)
    genre = project.genre

    if 'user_id' in session:
        if project.group_id == None:
            group_name = ''
        else:
            group_name = crud.get_group_name_by_project_name(project_name)
        
        return render_template('/project.html', project_name=project_name, genre=genre, group_name=group_name)


@app.route('/project', methods=["POST"])
def post_project():
    "Associate a Project with a Group"

    project_name = request.form.get("project_name")
    project = crud.get_project_by_name(project_name)
    group_name = request.form.get("group_name")
    group_id = crud.get_group_id_by_name(group_name)
    crud.add_group_to_project(group_id, project.project_id)
    return render_template('/project.html', project_name=project_name, genre=project.genre, group_name=group_name)



# @app.route('/project_page', methods=["GET"])
# def post_project_page():
#     """View Project Page BY Clicking Edit Project Button"""

#     #Returns Text From Submission
#     project = crud.get_project_by_name(project_name)
#     show_text = crud.get_text_for_project_page(project.project_id)

#     return render_template('project_page.html', project_name=project_name, show_text=show_text)


@app.route('/project_page', methods=["POST"])
def post_project_page():
    """View Project Page BY Clicking Edit Project Button"""

    #Creates A Submission
    project_name = request.form.get("project_name")
    text = request.form.get("text")
    crud.create_submission(project_name, text)
    return get_text_for_project_page(project_name)

    #Returns Text From Submission

def get_text_for_project_page(project_name):
    project = crud.get_project_by_name(project_name)
    show_text = crud.get_text_for_project_page(project.project_id)

    return render_template('project_page.html', project_name=project_name, show_text=show_text)


@app.route('/submit_project', methods=["POST"])
def submit_project__on_project_page():
    """Submit a Project to the Group"""

    project_name = request.form.get("project_name")
    crud.change_project_visibility(project_name)
    return get_text_for_project_page(project_name)


@app.route('/api/<group>/<name>')
def get_writer(group, name):
    """Returns Text For Given User"""
    group_id = crud.get_group_id_by_name(group)
    dict_of_users = crud.get_text_for_meeting_page(group_id)
    user = crud.get_user_by_name(name)
    full_name= user.first_name + " " + user.last_name
    if full_name in dict_of_users:
        return dict_of_users.get(full_name)
    else:
        return "user did not submit a project"


@app.route('/about')
def about_the_app():
    return "About the app"


""""Flask method which runs the app"""
if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug = True, host='0.0.0.0')