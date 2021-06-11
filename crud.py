"""CRUD operations for the writing app"""

from datetime import datetime
from model import db, User, Group, Project, Submission, Feedback, Character, Index, connect_to_db

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


def does_user_email_exist(email):

    return db.session.query(User).filter_by(email=email).first() is not None


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


def does_group_name_exist(group_name):

    return db.session.query(Group).filter_by(group_name=group_name).first() is not None


def delete_association(user_id, group_id):
    """Deletes An Association Between A User And A Group"""
    
    user = get_user_by_id(user_id)
 
    final_group = []

    for group in user.groups:
        if group.group_id == group_id:
            final_group.append(group)
            user.groups.remove(final_group[0])
            db.session.add(user)
            db.session.commit()

    


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


def does_project_name_exist(project_name):

    return db.session.query(Project).filter_by(project_name=project_name).first() is not None


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
    """Get Text From Submission By Project ID For The Project Page"""

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


def create_project_submission_solicit(project_name, text):
    """Updates A Submission For Project Solicitation"""

    project = get_project_by_name(project_name)
    submission = db.session.query(Submission).filter(Submission.project_id == project.project_id, Submission.text != None).order_by(Submission.submission_id.desc()).first()
    submission.project_submission_solicit = text
    db.session.add(submission)
    db.session.commit()


def solicit_feedback_for_meeting_page(group_id):
    """Get Project Feedback From Submission By Group ID For The Meeting Page"""
    
    list_of_projects = db.session.query(Project).filter(Project.group_id == group_id).all()
    
    final_result = {}
    
    for project in list_of_projects:
        if project.public == True:
            submission = db.session.query(Submission).filter(Submission.project_id == project.project_id, Submission.text != None).order_by(Submission.submission_id.desc()).first()
            user = get_user_by_id(submission.user_id)
            name = user.first_name + ' ' + user.last_name
            final_result[name] = submission.project_submission_solicit
    return final_result



def provide_feedback(user_id, group_name, feedback_text):
    """Provide Feedback For A Project On The Meeting Page; User_ID is the person providing feedback (the reviewer), not the one receiving it."""

    group_id = get_group_id_by_name(group_name)
    project = get_project_by_group_id(group_id)
    submission = db.session.query(Submission).filter(Submission.project_id == project.project_id, Submission.text != None).order_by(Submission.submission_id.desc()).first()
    if submission:
        feedback = Feedback(user_id=user_id, submission_id=submission.submission_id, text=feedback_text)
        db.session.add(feedback)
        db.session.commit()
    else:
        return "Sorry, we couldn't find that project."


def get_reviewer_feedback(project_name):
    """Gets User Feedback For Project Specific Page"""

    project = get_project_by_name(project_name)
    submission = db.session.query(Submission).filter(Submission.project_id == project.project_id, Submission.text != None).order_by(Submission.submission_id.desc()).first()
    
    
    if submission:
        list_of_reviewer_feedback = db.session.query(Feedback).filter(Feedback.submission_id == submission.submission_id, Feedback.text != None).all()
        feedback = Feedback.query.filter(Feedback.submission_id == submission.submission_id).all()
        final_result = {}
        for reviewer_feedback in list_of_reviewer_feedback:
            user = get_user_by_id(reviewer_feedback.user_id)
            name = user.first_name + ' ' + user.last_name
            final_result[name] = reviewer_feedback.text
        return final_result
    else:
        return ""    

def create_character(project_name, name, role, desc, age, physical_appearance, motivation, fondest_memory, song):
    """"Creates a Character"""

    project = get_project_by_name(project_name)
    character = Character(project_id=project.project_id, role=role, age=age, name=name, physical_appearance=physical_appearance, motivation=motivation, fondest_memory=fondest_memory, song=song, desc=desc)

    db.session.add(character)
    db.session.commit()

def create_index(name, desc, final_photo, projectName):
    """Creates a Index Card"""

    project = get_project_by_name(projectName)
    index = Index(project_id=project.project_id, name= name, desc=desc, index_url=final_photo)
    db.session.add(index)
    db.session.commit()


def get_all_cards(project_name):
    """Get all character and image cards by project id"""

    card_list = []
    project = get_project_by_name(project_name)
    characters = Character.query.filter(Character.project_id == project.project_id).all()
    images = Index.query.filter(Index.project_id == project.project_id).all()

    for character in characters:
        if characters == []:
            pass
        else:
            card_list.append(character)
    
    for image in images:
        if images == []:
            pass
        else:
            card_list.append(image)

    return card_list

def get_single_card(projectName, cardName):

    # card_name = cardName.lower()
    project = get_project_by_name(projectName)
    # character_card = Character.query.filter(Character.project_id == project.project_id, Character.name == card_name).first()
    image_card = Index.query.filter(Index.project_id == project.project_id, Index.name == cardName).first()

    dict_of_card = {'card_name': image_card.name, 'image_url': image_card.index_url, 'desc': image_card.desc}

    return dict_of_card

    # if character_card == []:
    #     return image_card
    # elif image_card == []:
    #     return character_card

if __name__=='__main__':
    from server import app
    connect_to_db(app)