"""CRUD operations for the writing app"""

from model import db, User, connect_to_db

def create_user(first_name, last_name, email, password, favorite_writer, favorite_animal):
    """Create and return a new user"""

    user = User(first_name=first_name, last_name=last_name, email=email, password=password, favorite_writer=favorite_writer, favorite_animal=favorite_animal)

    db.session.add(user)
    db.session.commit()

    return user


if __name__=='__main__':
    from server import app
    connect_to_db(app)