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
    submission = db.relationship('Submission', back_populates='user')
    feedback = db.relationship('Feedback', back_populates='user')

    def __repr__(self):
        return f'<User user_id={self.user_id} first_name={self.first_name} last_name={self.last_name} email={self.email}> password={self.password}'


class Group(db.Model):
    """A group."""

    __tablename__= 'groups'

    group_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    group_name = db.Column(db.String, unique=True)
    
    users = db.relationship('User', secondary=user_group_association, back_populates="groups")
    projects = db.relationship('Project', back_populates='group')

    def __repr__(self):
        return f'<Group group_id={self.group_id} group_name={self.group_name}>'


class Project(db.Model):
    """A project."""

    __tablename__= 'projects'

    project_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    project_name = db.Column(db.String, unique=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.group_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    genre = db.Column(db.String, nullable=True)
    public = db.Column(db.Boolean, default=False)
    

    user = db.relationship('User', back_populates='projects')
    group = db.relationship('Group', back_populates='projects')
    submission = db.relationship('Submission', back_populates='projects')
    character = db.relationship('Character', back_populates='projects')
    index = db.relationship('Index', back_populates='projects')
    storyarc = db.relationship('StoryArc', back_populates='projects')


    def __repr__(self):
        return f'<Project project_id={self.project_id} project_name={self.project_name} user_id={self.user_id} group_id={self.group_id} genre={self.genre}>'


class Submission(db.Model):
    """A submission."""

    __tablename__= 'submissions'

    submission_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'))
    meeting_time = db.Column(db.DateTime)
    project_submission_solicit = db.Column(db.String)
    text = db.Column(db.String)

    user = db.relationship('User', back_populates='submission')
    projects = db.relationship('Project', back_populates='submission')
    feedback = db.relationship('Feedback', back_populates='submission')

    def __repr__(self):
        return f'<Submission submission_id={self.submission_id} user_id={self.user_id} meeting_time={self.meeting_time} project_id={self.project_id} text={self.text} project_submission_solicit={self.project_submission_solicit}>'


class Feedback(db.Model):
    """Feedback"""

    __tablename__= 'feedback'

    feedback_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    submission_id = db.Column(db.Integer, db.ForeignKey('submissions.submission_id'))
    text = db.Column(db.String)

    user = db.relationship('User', back_populates='feedback')
    submission = db.relationship('Submission', back_populates='feedback')

    def __repr__(self):
        return f'<Feedback feedback_id={self.feedback_id} user_id={self.user_id} submission_id={self.submission_id} text={self.text}>'


class Character(db.Model):
    """Character"""

    __tablename__= 'character'

    character_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'))
    name = db.Column(db.String)
    role = db.Column(db.String)
    desc = db.Column(db.String)
    card_type = db.Column(db.String, default="character")
    age = db.Column(db.Integer)
    physical_appearance = db.Column(db.String)
    motivation = db.Column(db.String)
    fondest_memory = db.Column(db.String)
    song = db.Column(db.String) 

    projects = db.relationship('Project', back_populates='character')

    def __repr__(self):
        return f'<Character character_id={self.character_id} project_id={self.project_id} name={self.name} role={self.role} age={self.age} desc={self.desc}>'


class Index(db.Model):
    """Index Card"""

    __tablename__= "index"

    index_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'))
    index_url = db.Column(db.String)
    name = db.Column(db.String)
    desc = db.Column(db.String)
    card_type = db.Column(db.String, default="index")

    projects = db.relationship('Project', back_populates='index')

    def __repr__(self):
        return f'<Index index_id={self.index_id} project_id={self.index_id} index_url={self.index_url}>'


class StoryArc(db.Model):
    """Story Arc"""

    __tablename__="storyarc"

    storyarc_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'))
    storyarc_name = db.Column(db.String)
    plot_point1 = db.Column(db.String)
    plot_point1_value = db.Column(db.Integer)
    plot_point2 = db.Column(db.String)
    plot_point2_value = db.Column(db.Integer)
    plot_point3 = db.Column(db.String)
    plot_point3_value = db.Column(db.Integer)
    plot_point4 = db.Column(db.String)
    plot_point4_value = db.Column(db.Integer)
    plot_point5 = db.Column(db.String)
    plot_point5_value = db.Column(db.Integer)
    plot_point6 = db.Column(db.String)
    plot_point6_value = db.Column(db.Integer)

    projects = db.relationship('Project', back_populates='storyarc')

    def __repr__(self):
        return f'<StoryArc storyarc_id={self.storyarc} project_id={self.project_id}>'




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
