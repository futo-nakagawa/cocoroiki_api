from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
import models, schemas

#get all relation
def get_relation(session: Session):
    relation_list = session.query(models.RelationModel.Relation).all() # get all Relation items
    return relation_list 

#get relation by id
def get_relation_by_id(session: Session, id: int):
    relation = session.query(models.RelationModel.Relation).get(id) # get item with the given id
 
    # check if id exists. If not, return 404 not found response
    if not relation:
        raise HTTPException(status_code=404, detail=f"Relation item with id {id} not found")
 
    return relation

#create relation
def create_relation(session: Session, relation: schemas.RelationSchema.RelationCreate):
    relationdb = models.RelationModel.Relation(
        user_id = relation.user_id,
        family_id= relation.family_id
    )

    session.add(relationdb)
    session.commit()
    session.refresh(relationdb)
 
    return relationdb

#update relation by id
def update_relation(session: Session, relation: schemas.RelationSchema.RelationCreate, id: int):
    # Check if the Relation item with the given id exists
    existing_tree = session.query(models.RelationModel.Relation).get(id)
    if not existing_tree:
        raise HTTPException(status_code=404, detail=f"relation item with id {id} not found")

    # Update the attributes of the existing_tree with the values from the Relation parameter
    existing_tree.user_id = relation.user_id
    existing_tree.family_id = relation.family_id

    session.commit()
    session.refresh(existing_tree)

    return existing_tree


#delete relation by id
def delete_relation(session: Session, id: int):
    # get the given id
    relation = session.query(models.RelationModel.Relation).get(id)
 
    # if Relation item with given id exists, delete it from the database. Otherwise raise 404 error
    if relation:
        session.delete(relation)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"Relation item with id {id} not found")

    return {"message": f"relation item with id {id} is deleted successful"}