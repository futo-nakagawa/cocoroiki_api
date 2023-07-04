from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
import models, schemas

#get all user
def get_profile(session: Session): 
    profile_list = session.query(models.ProfileModel.Profile).all() # get all profile items
    return profile_list 

#get user by id
def get_profile_by_id(session: Session, id: int):     
    profile = session.query(models.ProfileModel.Profile).get(id) # get item with the given id
 
    # check if id exists. If not, return 404 not found response
    if not profile:
        raise HTTPException(status_code=404, detail=f"profile item with id {id} not found")
 
    return profile

#create user
def create_profile(session: Session, profile: schemas.ProfileSchema.ProfileCreate):
    profiledb = models.ProfileModel.Profile(
        name=profile.name,
        image=profile.image,
        content=profile.content
    )
 
    session.add(profiledb)
    session.commit()
    session.refresh(profiledb)
 
    return profiledb

#update user by id
def update_profile(session: Session, profile: schemas.ProfileSchema.ProfileCreate, id: int):
    # Check if the profile item with the given id exists
    existing_profile = session.query(models.ProfileModel.Profile).get(id)
    if not existing_profile:
        raise HTTPException(status_code=404, detail=f"profile item with id {id} not found")

    # Update the attributes of the existing_profile with the values from the profile parameter
    existing_profile.name = profile.name
    existing_profile.image = profile.image
    existing_profile.content = profile.content

    session.commit()
    session.refresh(existing_profile)

    return existing_profile

#delete user by id
def delete_profile(session: Session, id: int):
    # get the given id
    profile = session.query(models.ProfileModel.Profile).get(id)
 
    # if profile item with given id exists, delete it from the database. Otherwise raise 404 error
    if profile:
        session.delete(profile)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"profile item with id {id} not found")
  
    return {"message": f"profile item with id {id} is deleted successful"}