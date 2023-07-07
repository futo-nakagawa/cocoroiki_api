from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
import models, schemas

#get all closeness
def get_closeness(session: Session):
    closeness_list = (session.query(models.ClosenessModel.Closeness).all()) # get all closeness items
    return closeness_list 

#get closeness by id
def get_closeness_by_id(session: Session, id: int):
    close = session.query(models.ClosenessModel.Closeness).get(id) # get item with the given id
    # Check if close exists
    if not close:
        raise HTTPException(status_code=404, detail=f"Closeness with id {id} not found")

    return close

#create closeness
def create_closeness(session: Session, closeness: schemas.ClosenessSchema.ClosenessCreate):
    closenessdb = models.ClosenessModel.Closeness(
        tree_id=closeness.tree_id,
        close_meter=closeness.close_meter,
    )
 
    session.add(closenessdb)
    session.commit()
    session.refresh(closenessdb)

    return closenessdb

#update closeness by id
def update_closeness(session: Session, closeness: schemas.ClosenessSchema.ClosenessCreate, id: int):
        # Check if the closeness item with the given id exists
    existing_closeness = session.query(models.ClosenessModel.Closeness).get(id)
    if not existing_closeness:
        raise HTTPException(status_code=404, detail=f"Closeness item with id {id} not found")

    # Update the attributes of the existing_closeness with the values from the closeness parameter
    existing_closeness.tree_id = closeness.tree_id
    existing_closeness.close_meter = closeness.close_meter

    session.commit()
    session.refresh(existing_closeness)

    return existing_closeness

#delete closeness by id
def delete_closeness(session: Session, id: int):
        # get the given id
    closeness = session.query(models.ClosenessModel.Closeness).get(id)
 
    # if closeness item with given id exists, delete it from the database. Otherwise raise 404 error
    if closeness:
        session.delete(closeness)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"closeness item with id {id} not found")
    
    return {"message": f"closeness item with id {id} is deleted successful"}