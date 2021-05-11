#1. User1 signs up dolores@day.com test
    #a. log in 
    #b. create a Group Dolores Day
    #c. invites four people to the Group
    #d. creates a project 
    #e. submits a submission to the Group

#2. User2 signs up 
    #a. log in 
    #b. creates a project
    #c. creates a group
    #d. invites four people to the Group
    #e. submits a submission to the Group

#3. User3 signs up 
    #a. log in 
    #b. creates a project 
    #c. submits a submission to the Group

#4. User4 log in 
    #a. views group they've been invited to  
    #b. creates a project 
    #c. submits a submission to the Group

import os
import crud
import model
import server

os.system('dropdb writing_app')
os.system('createdb writing_app')

model.connect_to_db(server.app)
model.db.create_all()

crud.create_user(first_name='Test', last_name='User', email='test@test.com', password='test', favorite_writer='Hemingway', favorite_animal='monkeys')
crud.create_user(first_name='Test1', last_name='User1', email='test1@test.com', password='test', favorite_writer='Bronte', favorite_animal='pigs')


crud.create_group(group_name="Test")
crud.create_group(group_name="Test1")

