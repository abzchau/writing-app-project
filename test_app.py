from crud import create_user

def test_create_user(user):
    return create_user(first_name='mae', last_name='wong', email='mae@wong.com', password='test1', favorite_writer='Lessing', favorite_animal='dogs')

def test_capitalize_string():
    assert test_create_user() == '<User user_id=2 first_name=mae last_name=wong>'