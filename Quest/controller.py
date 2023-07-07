from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
import models, schemas

#get all quest
def get_quest(session: Session):
    quests_list = session.query(models.QuestModel.Quest).all() # get all quests items
    return quests_list 

#get quest by id
def get_quest_by_id(session: Session, id: int):
    quests = session.query(models.QuestModel.Quest).get(id) # get item with the given id
 
    # check if id exists. If not, return 404 not found response
    if not quests:
        raise HTTPException(status_code=404, detail=f"quests item with id {id} not found")
 
    return quests

#create quest
def create_quest(session: Session, quests: schemas.QuestSchema.QuestCreate):
    questsdb = models.QuestModel.Quest(
        content=quests.content,
        quest_kinds=quests.quest_kinds,
        completed=quests.completed
    )
 
    session.add(questsdb)
    session.commit()
    session.refresh(questsdb)
 
    return questsdb

#update quest by id
def update_quest(session: Session, quests: schemas.QuestSchema.QuestCreate, id: int):
    # Check if the quests item with the given id exists
    existing_quests = session.query(models.QuestModel.Quest).get(id)
    if not existing_quests:
        raise HTTPException(status_code=404, detail=f"quests item with id {id} not found")

    # Update the attributes of the existing_quests with the values from the quests parameter
    existing_quests.content=quests.content
    existing_quests.quest_kinds=quests.quest_kinds
    existing_quests.completed=quests.completed

    session.commit()
    session.refresh(existing_quests)

    return existing_quests

#delete quest by id
def delete_quest(session: Session, id: int):
    # get the given id
    quests = session.query(models.QuestModel.Quest).get(id)
 
    # if quests item with given id exists, delete it from the database. Otherwise raise 404 error
    if quests:
        session.delete(quests)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"quest item with id {id} not found")

    return {"message": f"quest item with id {id} is deleted successful"}