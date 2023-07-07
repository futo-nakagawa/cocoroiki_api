from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
import models, schemas

#get all user
def get_user(session: Session):
    users_list = session.query(models.AppUserModel.AppUser).all() # get all users items
    return users_list 

#get user by id
def get_user_by_id(session: Session, id: int):
    user = session.query(models.AppUserModel.AppUser).get(id) # get item with the given id

    # Check if user exists
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")

    return user

#create user
def create_user(session: Session, users: schemas.AppUserSchema.AppUserCreate):
    usersdb = models.AppUserModel.AppUser(
        name=users.name,
        email=users.email,
        password=users.password,
        birth=users.birth,
        age=users.age,
        gender=users.gender,
        quest_role=users.quest_role,
        family_id=users.family_id,
        grandparent=users.grandparent,
        last_login=datetime.today(),
        createdAt=datetime.today(),
        updatedAt=datetime.today(),
        publishedAt=datetime.today()
    )
 
    session.add(usersdb)
    session.commit()
    session.refresh(usersdb)

    return usersdb

#update user by id
def update_user(session: Session, users: schemas.AppUserSchema.AppUserCreate, id: int):
    # Check if the users item with the given id exists
    existing_users = session.query(models.AppUserModel.AppUser).get(id)
    if not existing_users:
        raise HTTPException(status_code=404, detail=f"users item with id {id} not found")

    # Update the attributes of the existing_users with the values from the users parameter
    existing_users.name = users.name
    existing_users.email = users.email
    existing_users.password = users.password
    existing_users.birth = users.birth
    existing_users.age = users.age
    existing_users.gender = users.gender
    existing_users.quest_role = users.quest_role
    existing_users.family_id = users.family_id
    existing_users.grandparent = users.grandparent

    session.commit()
    session.refresh(existing_users)

    return existing_users

#delete user by id
def delete_user(session: Session, id: int):
    # get the given id
    users = session.query(models.AppUserModel.AppUser).get(id)
 
    # if users item with given id exists, delete it from the database. Otherwise raise 404 error
    if users:
        session.delete(users)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"users item with id {id} not found")
 
    return {"message": f"users item with id {id} is deleted successful"}