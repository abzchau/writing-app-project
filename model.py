"""Models for writing app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

"""db object - represents our database"""
db = SQLAlchemy()


user_group_association = db.Table('user_group_association',
    db.Column('user_id', db.Integer, db.ForeignKey('users.user_id')),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.group_id'))
)

class User(db.Model):
    """A user."""

    __tablename__= 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    favorite_writer = db.Column(db.String, nullable=True)
    favorite_animal = db.Column(db.String, nullable=True)

    groups = db.relationship('Group', secondary=user_group_association, back_populates='users')
    projects = db.relationship('Project', back_populates='user')
    # user_group = db.relationship('UserGroup', back_populates='user')
    submission = db.relationship('Submission', back_populates='user')
    feedback = db.relationship('Feedback', back_populates='user')

    def __repr__(self):
        return f'<User user_id={self.user_id} first_name={self.first_name} last_name={self.last_name} email={self.email}> password={self.password}'


class Group(db.Model):
    """A group."""

    __tablename__= 'groups'

    group_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    group_name = db.Column(db.String)
    
    users = db.relationship('User', secondary=user_group_association, back_populates="groups")
    projects = db.relationship('Project', back_populates='group')
    # user_group = db.relationship('UserGroup', back_populates='group')

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
    public = db.Column(db.Boolean, default=False)
    

    user = db.relationship('User', back_populates='projects')
    group = db.relationship('Group', back_populates='projects')
    submission = db.relationship('Submission', back_populates='projects')

    def __repr__(self):
        return f'<Project project_id={self.project_id} project_name={self.project_name} user_id={self.user_id} group_id={self.group_id} genre={self.genre}>'


class Submission(db.Model):
    """A submission."""

    __tablename__= 'submissions'

    submission_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'))
    meeting_time = db.Column(db.DateTime)
    project_feedback = db.Column(db.String)
    text = db.Column(db.String)

    user = db.relationship('User', back_populates='submission')
    projects = db.relationship('Project', back_populates='submission')
    feedback = db.relationship('Feedback', back_populates='submission')

    def __repr__(self):
        return f'<Submission submission_id={self.submission_id} user_id={self.user_id} meeting_time={self.meeting_time} project_id={self.project_id} text={self.text} project_feedback={self.project_feedback}>'


class Feedback(db.Model):
    """Feedback."""

    __tablename__= 'feedback'

    feedback_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    submission_id = db.Column(db.Integer, db.ForeignKey('submissions.submission_id'))
    text = db.Column(db.String)

    user = db.relationship('User', back_populates='feedback')
    submission = db.relationship('Submission', back_populates='feedback')

    def __repr__(self):
        return f'<Feedback feedback_id={self.feedback_id} user_id={self.user_id} submission_id={self.submission_id} text={self.text}>'


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
