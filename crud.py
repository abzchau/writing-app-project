"""CRUD operations for the writing app"""

from datetime import datetime
from model import db, User, Group, Project, Submission, Feedback, connect_to_db

def create_user(first_name, last_name, email, password, favorite_writer="", favorite_animal=""):
    """Create and return a new user"""

    user = User(first_name=first_name, last_name=last_name, email=email, password=password, favorite_writer=favorite_writer, favorite_animal=favorite_animal)

    db.session.add(user)
    db.session.commit()

    return user


def get_user_by_id(user_id):
    """Get a user by id"""

    user = User.query.filter(User.user_id == user_id).first()
    return user


def get_user_by_email(email):
    """Get a user by email"""

    user = User.query.filter(User.email == email).first()
    return user


def create_group(group_name):
    """Create a group"""

    group = Group(group_name=group_name)
    db.session.add(group)
    db.session.commit()
    return group


def get_group_by_id(group_id):
    """Get a group by group id"""

    group = Group.query.filter(Group.group_id == group_id).first()
    return group


def get_group_id_by_name(group_name):
    """Get a group id by group name"""

    group = Group.query.filter_by(group_name=group_name).first()
    return group.group_id


def get_group_name_by_project_name(project_name):
    """"Get a group name by project name"""

    project = get_project_by_name(project_name)
    group = get_group_by_id(project.group_id)
    return group.group_name


def create_project(project_name, user_id, genre=""):
    """Create and return a new project"""

    project = Project(project_name=project_name, user_id=user_id, genre=genre)
    db.session.add(project)
    db.session.commit()

    return project

def get_project_by_name(project_name):
    """Get a Project by project name"""

    project = Project.query.filter_by(project_name=project_name).first()
    return project


def create_association(group: Group, user: User):
    """Creates association when a user creates a group"""
    
    group.users.append(user) 

    db.session.add(group)
    
    db.session.commit()



def add_group_to_project(group_id, project_id):
    """Add group to a project"""

    project = Project.query.get(project_id)
    print('this actually happened', project.group_id)
    project.group_id = group_id
    db.session.commit()
    
    return project


def create_submission(project_name, text):
    """Creates a submission when a user saves a project"""

    project = get_project_by_name(project_name)
    project_id = project.project_id
    user_id = project.project_name
    submission = Submission(project_id=project_id, user_id=project.user_id, text=text)
    db.session.add(submission)
    db.session.commit()
    return submission


def get_all_groups_by_user(user_id):
    """Get a list of all groups by User ID"""

    user = User.query.get(user_id)

    return user.groups


def get_all_projects_by_user(user_id):
    """Get a list of all groups by User ID"""

    user = User.query.get(user_id)

    return user.projects


def get_all_users_of_a_group(group_id):
    """Get a list of all groups by User ID"""

    group = Group.query.get(group_id)

    return group.users


def change_project_visibility(project_name):
    """Change Project Visibility to Public"""

    project = Project.query.filter_by(project_name=project_name).first()
    project.public = True
    db.session.add(project)
    db.session.commit()



def get_text_for_meeting_page(group_id):
    """Get Text From Submission By Group ID"""

    list_of_projects = db.session.query(Project).filter(Project.group_id == group_id).all()
    
    for project in list_of_projects:
        final_result = {}
        if project.public == True:
            submission = db.session.query(Submission).filter(Submission.project_id == project.project_id).order_by(Submission.submission_id.desc()).first()
            final_result[submission.user_id] = submission.text
    return final_result



    
# def get_submission_by_project_id(project_id):
#     """Get a submission by project id"""

#     submission = Submission.query.filter_by(project_id=project_id).first()
#     return submission.text



# def save_project(project_id, submission_id, user_id, text):

#     project = Project.query.get(project_id)
#     project.user_id = user_id
#     project.text = text



# def create_submission(meeting_time):
#     """Create and return a submission"""

#     submission = Submission(meeting_time=meeting_time)

#     db.session.add(submission)
#     db.session.commit()

#     return submission


# def create_feedback(text):
#     """Create and return feedback on a submission"""

#     feedback = Feedback(text=text)

#     db.session.add(feedback)
#     db.session.commit()

#     return feedback


# def get_all_users_of_a_group(group_id):
#     """Get all users of a group"""

#     users_by_group = UserGroup.query.filter_by(group_id=group_id).all()
#     return users_by_group


# def get_get_group_by_user(user_id):
#     """Get all groups by user"""

#     group_by_user = UserGroup.query.filter_by(group_id=group_id).all()
#     return group_by_user



if __name__=='__main__':
    from server import app
    connect_to_db(app)