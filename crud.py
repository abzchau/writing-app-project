"""CRUD operations for the writing app"""

from model import db, User, Group, Project, connect_to_db

def create_user(first_name, last_name, email, password, favorite_writer, favorite_animal):
    """Create and return a new user"""

    user = User(first_name=first_name, last_name=last_name, email=email, password=password, favorite_writer=favorite_writer, favorite_animal=favorite_animal)

    db.session.add(user)
    db.session.commit()

    return user


def create_group(group_name):
    """Create and return a new group"""

    group = Group(group_name=group_name)

    db.session.add(group)
    db.session.commit()

    return group


def create_project(project_name, genre):
    """Create and return a new project"""

    project = Project(project_name=project_name, genre=genre)

    db.session.add(project)
    db.session.commit()

    return project


if __name__=='__main__':
    from server import app
    connect_to_db(app)