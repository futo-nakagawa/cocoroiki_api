from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
import models, schemas

#get all quest_type
def get_quest_type(session: Session):
    questtype_list = session.query(models.QuestTypeModel.QuestType).all() # get all QuestType items
    return questtype_list 

#get quest_type by id
def get_quest_type_by_id(session: Session, id: int):
    questtype = session.query(models.QuestTypeModel.QuestType).get(id) # get item with the given id
 
    # check if id exists. If not, return 404 not found response
    if not questtype:
        raise HTTPException(status_code=404, detail=f"questtype item with id {id} not found")
 
    return questtype

#create quest_type
def create_quest_type(session: Session, questtype: schemas.QuestTypeSchema.QuestTypeCreate):
    questtypedb = models.QuestTypeModel.QuestType(
        kinds = questtype.kinds,
        online = questtype.online
    )

    session.add(questtypedb)
    session.commit()
    session.refresh(questtypedb)
 
    return questtypedb

#update quest_type by id
def update_quest_type(session: Session, questtype: schemas.QuestTypeSchema.QuestTypeCreate, id: int):
    # Check if the questtype item with the given id exists
    existing_tree = session.query(models.QuestTypeModel.QuestType).get(id)
    if not existing_tree:
        raise HTTPException(status_code=404, detail=f"QuestType item with id {id} not found")

    # Update the attributes of the existing_tree with the values from the questtype parameter
    existing_tree.kinds = questtype.kinds
    existing_tree.online = questtype.online

    session.commit()
    session.refresh(existing_tree)

    return existing_tree


#delete quest_type by id
def delete_quest_type(session: Session, id: int):
    # get the given id
    questtype = session.query(models.QuestTypeModel.QuestType).get(id)
 
    # if questtype item with given id exists, delete it from the database. Otherwise raise 404 error
    if questtype:
        session.delete(questtype)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"questtype item with id {id} not found")

    return {"message": f"quest_type item with id {id} is deleted successful"}