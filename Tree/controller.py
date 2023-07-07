from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
import models, schemas

#get all tree
def get_tree(session: Session):
    tree_list = session.query(models.TreeModel.Tree).all() # get all Tree items
    return tree_list

#get tree by id
def get_tree_by_id(session: Session, id: int):
    tree = session.query(models.TreeModel.Tree).get(id) # get item with the given id
 
    # check if id exists. If not, return 404 not found response
    if not tree:
        raise HTTPException(status_code=404, detail=f"tree item with id {id} not found")
 
    return tree


#create tree
def create_tree(session: Session, tree: schemas.TreeSchema.TreeCreate):
    treedb = models.TreeModel.Tree(
        growth_stage = tree.growth_stage,
        quest = tree.quest,
        watering = datetime.today()
    )
 
    session.add(treedb)
    session.commit()
    session.refresh(treedb)
 
    return treedb

#update tree by id
def update_tree(session: Session, tree: schemas.TreeSchema.TreeCreate, id: int):
    # Check if the tree item with the given id exists
    existing_tree = session.query(models.TreeModel.Tree).get(id)
    if not existing_tree:
        raise HTTPException(status_code=404, detail=f"Tree item with id {id} not found")

    # Update the attributes of the existing_tree with the values from the tree parameter
    existing_tree.growth_stage = tree.growth_stage
    existing_tree.quest = tree.quest

    session.commit()
    session.refresh(existing_tree)

    return existing_tree

#delete tree by id
def delete_tree(session: Session, id: int):
    # get the given id
    tree = session.query(models.TreeModel.Tree).get(id)
 
    # if tree item with given id exists, delete it from the database. Otherwise raise 404 error
    if tree:
        session.delete(tree)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"tree item with id {id} not found")

    return {"message": f"tree item with id {id} is deleted successful"}