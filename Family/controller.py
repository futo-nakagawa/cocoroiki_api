from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
import models, schemas

#get all family
def get_family(session: Session):
    family_list = session.query(models.FamilyModel.Family).all() # get all family items
    return family_list 

#get family by id
def get_family_by_id(session: Session, id: int):
    family = session.query(models.FamilyModel.Family).get(id) # get item with the given id
 
    # check if id exists. If not, return 404 not found response
    if not family:
        raise HTTPException(status_code=404, detail=f"family item with id {id} not found")
 
    return family

#create family
def create_family(session: Session, family: schemas.FamilySchema.FamilyCreate):
    familydb = models.FamilyModel.Family(
        name=family.name,
        total=family.total,
        createdAt=datetime.today(),
        updatedAt=datetime.today()
    )
 
    session.add(familydb)
    session.commit()
    session.refresh(familydb)
 
    return familydb

#update family by id
def update_family(session: Session, family: schemas.FamilySchema.FamilyCreate, id: int):
    # Check if the family item with the given id exists
    existing_family = session.query(models.FamilyModel.Family).get(id)
    if not existing_family:
        raise HTTPException(status_code=404, detail=f"family item with id {id} not found")

    # Update the attributes of the existing_family with the values from the family parameter
    existing_family.name=family.name
    existing_family.total=family.total

    session.commit()
    session.refresh(existing_family)

    return existing_family

#delete family by id
def delete_family(session: Session, id: int):
    # get the given id
    family = session.query(models.FamilyModel.Family).get(id)
 
    # if family item with given id exists, delete it from the database. Otherwise raise 404 error
    if family:
        session.delete(family)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"family item with id {id} not found")
 
    return {"message": f"family item with id {id} is deleted successful"}