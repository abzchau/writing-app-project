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

#HOMEPAGE / LOG IN / SIGN UP PAGES / About Us

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
            return redirect(url_for("view_main"))

  
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


@app.route('/about')
def about_the_app():
    return "About the app"

#Main Page Where User Can View And Create Groups And Projects

@app.route('/main', methods=["GET"])
def view_main():
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
        if crud.does_group_name_exist(request.form.get("group_name")):
            flash('A Group with that name already exists. Please choose another Group name.')
            return view_main()
        else:
            group_name = request.form.get("group_name")
            group = crud.create_group(group_name)
            session["group_id"] = group.group_id
            user_id = session["user_id"]
            user = crud.get_user_by_id(user_id)
            crud.create_association(group, user)
            flash('Group Created')
            return redirect(f"/group/{group_name}")
    
    if "project_name" in request.form:
        if crud.does_project_name_exist(request.form.get("project_name")):
            flash('A Project with that name already exists. Please choose another Project name.')
            return view_main()
        else:    
            user_id = session["user_id"]
            project_name = request.form.get("project_name")
            genre = request.form.get("genre")
            project = crud.create_project(project_name, user_id, genre)
            flash('Project Created')
            return redirect(f"/project/{project_name}")


#Group Page Where User Can Add Members And View Meeting Page 

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
    """Add a user to a group"""
    
    email = request.form.get("email")
    remove_email = request.form.get("remove_user_email")
    add_user = request.form.get("add_user")
    remove_user = request.form.get("remove_user")
    group_name = request.form.get("group_name")
    
    
    group_id = crud.get_group_id_by_name(group_name)
    group = crud.get_group_by_id(group_id)

    if add_user:
        if crud.does_user_email_exist(email):
            user = crud.get_user_by_email(email)
            crud.create_association(group, user)
        else:
            flash("The user does not exist. Please try again, or have the user sign up.")
            return redirect(f"/group/{group_name}") 
    elif remove_user:
        if crud.does_user_email_exist(remove_email):
            user = crud.get_user_by_email(remove_email)
            crud.delete_association(user.user_id, group_id)
            flash(f'{remove_email} has been removed from the {group_name}.')
        else:
            flash("The user does not exist. Please try again, or have the user sign up.")
            return redirect(f"/group/{group_name}") 
    
    lst_of_groups_by_user_id = crud.get_all_groups_by_user(user.user_id)
    lst_of_users_by_group = group.users        
    return render_template("/group.html", group_name=group_name, lst_of_groups_by_user_id=lst_of_groups_by_user_id, lst_of_users_by_group=lst_of_users_by_group)



#Meeting Page Where All Users of A Group Meets And Users Can View Feedback Wanted And Provide Feedback 

@app.route('/meeting_page', methods=["GET", "POST"])
def meeting_page():
    """View the Group's Meeting Page; Users Can Provide Feedback Which Will Be Viewable On The Project Page"""

    if 'user_id' in session:
        user_id = session['user_id']
        group_name = request.form.get("group_name")
        group_id = crud.get_group_id_by_name(group_name)
        group = crud.get_group_by_id(group_id)
        lst_of_users_by_group = group.users

        #This section gets the feedback from the form and creates a Feedback which will be viewable on the Project Page.
        feedback_text = request.form.get("provide-feedback")
        crud.provide_feedback(user_id, group_name, feedback_text)

        #This section is to retrieve the text
        dict_of_users = crud.get_text_for_meeting_page(group_id)
        return render_template('/meeting_page.html', group_name=group_name, lst_of_users_by_group=lst_of_users_by_group, dict_of_users=dict_of_users)


@app.route('/api/<group>/<name>')
def get_writer(group, name):
    """Returns Text On Meeting Page For Given User"""

    group_id = crud.get_group_id_by_name(group)
    dict_of_users = crud.get_text_for_meeting_page(group_id)
    user = crud.get_user_by_name(name)
    full_name= user.first_name + " " + user.last_name
    if full_name in dict_of_users:
        return dict_of_users.get(full_name)
    else:
        return "user did not submit a project"

@app.route('/api/<group>/<name>/feedback')
def solicit_feedback(group, name):
    """Solicit Feedback On Meeting Page; The User Enters Feedback Wanted On the Project Page"""

    group_id = crud.get_group_id_by_name(group)
    dict_project_feedback = crud.solicit_feedback_for_meeting_page(group_id)

    user = crud.get_user_by_name(name)
    full_name= user.first_name + " " + user.last_name
    if full_name in dict_project_feedback:
        return dict_project_feedback.get(full_name)
    else:
        return "user did not submit a project"


#Project Page Where Users Can View And Create Projects And Associate Projects With Groups And Edit Projects

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


@app.route('/create_character', methods=["POST"])
def create_character():

    project_name = request.form.get("project_name")

    name = request.form.get("name")
    role = request.form.get("role")
    age = request.form.get("age")
    physical_appearance = request.form.get("appearance")
    motivation = request.form.get("motivation")
    fondest_memory = request.form.get("memory")
    song = request.form.get("song")
    desc = request.form.get("desc")
    character = crud.create_character(project_name, name, role, desc, age, physical_appearance, motivation, fondest_memory, song)


    return get_text_for_project_page(project_name)

@app.route('/api/<name>/<desc>/<photoNum>/<photoReplacedFinal>/<projectName>')
def create_postcard(name, desc, photoNum, photoReplacedFinal, projectName):
    """Create a postcard on the project page for it to appear on the project specific page"""

    project_name = projectName

    #Process photo by rebuilding the image url received from the server

    photo = 'https://images.pexels.com/photos/'
    photo_replace_ampersand =  photoReplacedFinal.replace('replace', '&')
    photo_replace_question_mark =  photo_replace_ampersand.replace('question', '?')
    final_photo = photo + photoNum + '/' + photo_replace_question_mark
    postcard = crud.create_postcard(name, desc, final_photo, projectName)
    return get_text_for_project_page(project_name)

#Project-Specific Page Where You Can Edit A Project, Submit A Project And View Feedback From Other Users About Your Project

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
    """"""

    project = crud.get_project_by_name(project_name)
    show_text = crud.get_text_for_project_page(project.project_id)
    dict_of_reviewers = crud.get_reviewer_feedback(project_name)

    return render_template('project_page.html', project_name=project_name, show_text=show_text, dict_of_reviewers=dict_of_reviewers)

@app.route('/submit_project', methods=["POST"])
def submit_project__on_project_page():
    """Submit a Project to the Group"""

    project_name = request.form.get("project_name")
    text = request.form.get("text")
    crud.change_project_visibility(project_name)
    crud.create_project_submission_solicit(project_name, text)
    return get_text_for_project_page(project_name)


@app.route('/api/project/<project>/<name>')
def get_reviewer(project, name):
    """Returns Text For Reviewer's Feedback On Project Page"""

    project_name = project
    dict_of_reviewers = crud.get_reviewer_feedback(project_name)
    if name in dict_of_reviewers:
        return dict_of_reviewers.get(name)


""""Flask method which runs the app"""
if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug = True, host='0.0.0.0')