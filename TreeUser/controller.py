from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
import models, schemas

#get all tree_user
def get_tree_user(session: Session):
    tree_user_list = session.query(models.TreeUserModel.TreeUser).all() # get all TreeUser items
    return tree_user_list 

#get tree_user by id
def get_tree_user_by_id(session: Session, id: int):
    tree_user = session.query(models.TreeUserModel.TreeUser).get(id) # get item with the given id
 
    # check if id exists. If not, return 404 not found response
    if not tree_user:
        raise HTTPException(status_code=404, detail=f"TreeUser item with id {id} not found")
 
    return tree_user

#create tree_user
def create_tree_user(session: Session, tree_user: schemas.TreeUserSchema.TreeUserCreate):
    tree_userdb = models.TreeUserModel.TreeUser(
        tree_id= tree_user.tree_id,
        user_id = tree_user.user_id
    )

    session.add(tree_userdb)
    session.commit()
    session.refresh(tree_userdb)
 
    return tree_userdb

#update tree_user by id
def update_tree_user(session: Session, tree_user: schemas.TreeUserSchema.TreeUserCreate, id: int):
    # Check if the TreeUser item with the given id exists
    existing_tree = session.query(models.TreeUserModel.TreeUser).get(id)
    if not existing_tree:
        raise HTTPException(status_code=404, detail=f"tree_user item with id {id} not found")

    # Update the attributes of the existing_tree with the values from the TreeUser parameter
    existing_tree.tree_id = tree_user.tree_id
    existing_tree.user_id = tree_user.user_id

    session.commit()
    session.refresh(existing_tree)

    return existing_tree


#delete tree_user by id
def delete_tree_user(session: Session, id: int):
    # get the given id
    tree_user = session.query(models.TreeUserModel.TreeUser).get(id)
 
    # if TreeUser item with given id exists, delete it from the database. Otherwise raise 404 error
    if tree_user:
        session.delete(tree_user)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"TreeUser item with id {id} not found")

    return {"message": f"tree_user item with id {id} is deleted successful"}