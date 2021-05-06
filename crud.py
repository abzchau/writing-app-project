"""CRUD operations for the writing app"""

from datetime import datetime
from model import db, User, Group, Project, Submission, UserGroup, Feedback, connect_to_db

def create_user(first_name, last_name, email, password, favorite_writer=None, favorite_animal=None):
    """Create and return a new user"""

    user = User(first_name=first_name, last_name=last_name, email=email, password=password, favorite_writer=favorite_writer, favorite_animal=favorite_animal)

    db.session.add(user)
    db.session.commit()

    return user


def get_user_by_email(email):
    """Get a user by email"""

    user = User.query.filter(User.email == email).first()
    return user



def create_group(group_name):
    """Create and return a new group"""

    group = Group(group_name=group_name)

    db.session.add(group)
    db.session.commit()

    return group


def get_group_id(group_id):
    """Return group id"""

    group = Group(group_name=group_name)

    db.session.add(group)
    db.session.commit()

    return group


def create_project(project_name, user_id, group_id, genre=""):
    """Create and return a new project"""
    print('Attempting to create project...')
    project = Project(project_name=project_name, user_id=user_id, group_id=1, genre=genre)
    print(project)
    db.session.add(project)
    db.session.commit()

    return project


def create_member(user_id, group_id):
    """Create and return a new User Group"""
    user_group = UserGroup(user_id=user_id, group_id=group_id)
    db.session.add(user_group)
    db.session.commit()

    return user_group

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



if __name__=='__main__':
    from server import app
    connect_to_db(app)