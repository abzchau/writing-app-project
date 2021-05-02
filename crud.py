"""CRUD operations for the writing app"""

from datetime import datetime
from model import db, User, Group, Project, Submission, UserGroup, Feedback, connect_to_db

def create_user(user_id, first_name, last_name, email, password, favorite_writer, favorite_animal):
    """Create and return a new user"""

    user = User(user_id=user_id, first_name=first_name, last_name=last_name, email=email, password=password, favorite_writer=favorite_writer, favorite_animal=favorite_animal)

    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_email(email):
    """Return a user by email"""

    return User.query.filter(User.email == email).first()


def create_group(group_name):
    """Create and return a new group"""

    group = Group(group_name=group_name)

    db.session.add(group)
    db.session.commit()

    return group


def create_project(project_name, user_id, genre):
    """Create and return a new project"""

    project = Project(project_name=project_name, user_id= user_id, genre=genre)

    db.session.add(project)
    db.session.commit()

    return project


def create_submission(meeting_time):
    """Create and return a submission"""

    submission = Submission(meeting_time=meeting_time)

    db.session.add(submission)
    db.session.commit()

    return submission


def create_feedback(text):
    """Create and return feedback on a submission"""

    feedback = Feedback(text=text)

    db.session.add(feedback)
    db.session.commit()

    return feedback



if __name__=='__main__':
    from server import app
    connect_to_db(app)