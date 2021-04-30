"""Models for writing app."""

from flask_sqlalchemy import SQLAlchemy

"""db object - represents our database"""
db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__= 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    favorite_writer = db.Column(db.String, nullable=True)
    favorite_animal = db.Column(db.String, nullable=True)

    projects = db.relationship('Project')

    def __repr__(self):
        return f'<User user_id={self.user_id} first_name={self.first_name} last_name={self.last_name}>'


class Group(db.Model):
    """A group."""

    __tablename__= 'groups'

    group_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    group_name = db.Column(db.String)


    projects = db.relationship('Project')

    def __repr__(self):
        return f'<Group group_id={self.group_id} group_name={self.group_name}>'


class Project(db.Model):
    """A project."""

    __tablename__= 'projects'

    project_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    project_name = db.Column(db.String)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.group_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    genre = db.Column(db.String, nullable=True)

    user = db.relationship('User')
    group = db.relationship('Group')

    def __repr__(self):
        return f'<Project project_id={self.project_id} project_name={self.project_name} user_id={self.user_id} group_id={self.group_id}>'


    
def connect_to_db(flask_app, db_uri='postgresql:///writing_app', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Whoop, connected to the database!')


if __name__ == '__main__':
    from server import app


    connect_to_db(app)
