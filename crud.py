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


def get_user_by_name(user_name):
    """Get a user by id"""
    name = user_name.split()
    first_name = name[0]
    last_name = name[1]
    user = User.query.filter(User.first_name == first_name, User.last_name == last_name).first()
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


def get_project_by_group_id(group_id):
    """Get a Project by Group ID"""

    project = Project.query.filter_by(group_id=group_id).first()
    
    return project


def create_association(group: Group, user: User):
    """Creates association when a user creates a group"""
    
    group.users.append(user) 

    db.session.add(group)
    
    db.session.commit()



def add_group_to_project(group_id, project_id):
    """Add group to a project"""

    project = Project.query.get(project_id)
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



def get_text_for_project_page(project_id):
    """Get Text From Submission By Project ID For The Meeting Page"""

    submission = db.session.query(Submission).filter(Submission.project_id == project_id, Submission.text != None).order_by(Submission.submission_id.desc()).first()
    
    if not submission:
        return ''
    else:
        return submission.text

def get_text_for_meeting_page(group_id):
    """Get Text From Submission By Group ID For The Meeting Page"""

    list_of_projects = db.session.query(Project).filter(Project.group_id == group_id).all()
    
    final_result = {}
    
    for project in list_of_projects:
        if project.public == True:
            submission = db.session.query(Submission).filter(Submission.project_id == project.project_id, Submission.text != None).order_by(Submission.submission_id.desc()).first()
            user = get_user_by_id(submission.user_id)
            name = user.first_name + ' ' + user.last_name
            final_result[name] = submission.text
    return final_result


def create_project_feedback(project_name, text):
    """Updates Project Feedback On A Submission"""

    project = get_project_by_name(project_name)
    submission = db.session.query(Submission).filter(Submission.project_id == project.project_id, Submission.text != None).order_by(Submission.submission_id.desc()).first()
    submission.project_feedback = text
    db.session.add(submission)
    db.session.commit()


def give_me_feedback_for_meeting_page(group_id):
    """Get Project Feedback From Submission By Group ID For The Meeting Page"""
    
    list_of_projects = db.session.query(Project).filter(Project.group_id == group_id).all()
    
    final_result = {}
    
    for project in list_of_projects:
        if project.public == True:
            submission = db.session.query(Submission).filter(Submission.project_id == project.project_id, Submission.text != None).order_by(Submission.submission_id.desc()).first()
            user = get_user_by_id(submission.user_id)
            name = user.first_name + ' ' + user.last_name
            final_result[name] = submission.project_feedback
    return final_result


# def create_feedback(user_id, project_name, text):
#     """Creates Feedback For A Project"""

#     project = get_project_by_name(project_name)
#     submission = db.session.query(Submission).filter(Submission.project_id == project.project_id, Submission.text != None).order_by(Submission.submission_id.desc()).first()
#     if submission:
#         feedback = Feedback(user_id=project.user_id, submission_id=submission.submission_id, text=text)
#         db.session.add(feedback)
#         db.session.commit()
#     else:
#         pass

# def get_feedback_for_group_page(group_name):
#     """Returns Feedback Text For The Meeting Page"""
#     project = get_project_by_group_name(group_name)
#     submission = db.session.query(Submission).filter(Submission.project_id == project_id, Submission.text != None).order_by(Submission.submission_id.desc()).first()
#     feedback = Feedback.query.filter(Feedback.submission_id == submission.submission_id).first() 
#     return feedback.text

# def get_project_feedback(group_id):
#     """Get Project Feedback"""

#     project = get_project_by_group_id(group_id)
#     submission = db.session.query(Submission).filter(Submission.project_id == project.project_id, Submission.text != None).order_by(Submission.submission_id.desc()).first()
#     return submission.project_feedback



if __name__=='__main__':
    from server import app
    connect_to_db(app)