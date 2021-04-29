from crud import create_user
from model import connect_to_db

def test_create_user(user):
    connect_to_db(app)
    user = create_user(first_name='mae', last_name='wong', email='mae@wong.com', password='test1', favorite_writer='Lessing', favorite_animal='dogs')
    return user

def test_capitalize_string():
    assert test_create_user(user) == '<User user_id=2 first_name=mae last_name=wong>'



