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


#Creates test users
crud.create_user(first_name='Test1', last_name='User', email='test1@test.com', password='test', favorite_writer='Hemingway', favorite_animal='monkeys')
crud.create_user(first_name='Test2', last_name='User1', email='test2@test.com', password='test', favorite_writer='Bronte', favorite_animal='pigs')
crud.create_user(first_name='Mae', last_name='Wong', email='mae@wong.com', password='test', favorite_writer='Lessing', favorite_animal='dogs')

#Creates groups 
crud.create_group(group_name="Group1")
crud.create_group(group_name="Group2")

#Creates association between user and group
group1 = crud.get_group_by_id(1)
user1 = crud.get_user_by_id(1)
crud.create_association(group=group1, user=user1)

group2 = crud.get_group_by_id(2)
user2 = crud.get_user_by_id(2)
crud.create_association(group=group2, user=user2)

#Creates projects
crud.create_project(project_name="Project1", user_id=1, genre='YA')
crud.create_project(project_name="Project2", user_id=2, genre='Romance')

#Associates a group to a project
crud.add_group_to_project(group_id=1, project_id=1)
crud.add_group_to_project(group_id=2, project_id=2)

