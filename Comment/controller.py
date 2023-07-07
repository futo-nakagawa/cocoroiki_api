from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
import models, schemas

#get all comment
def get_comment(session: Session):
    comment_list = session.query(models.CommentModel.Comment).all() # get all Comment items
    return comment_list 

#get comment by id
def get_comment_by_id(session: Session, id: int):
    comment = session.query(models.CommentModel.Comment).get(id) # get item with the given id
 
    # check if id exists. If not, return 404 not found response
    if not comment:
        raise HTTPException(status_code=404, detail=f"comment item with id {id} not found")
 
    return comment


#create comment
def create_comment(session: Session, comment: schemas.CommentSchema.CommentCreate):
    commentdb = models.CommentModel.Comment(
        parent_id = comment.parent_id,
        post_id = comment.post_id,
        user_id = comment.user_id,
        content = comment.content,
        createdAt= datetime.today()
    )
 
    session.add(commentdb)
    session.commit()
    session.refresh(commentdb)
 
    return commentdb

#update comment by id
def update_comment(session: Session, comment: schemas.CommentSchema.CommentCreate, id: int):
    # Check if the comment item with the given id exists
    existing_comment = session.query(models.CommentModel.Comment).get(id)
    if not existing_comment:
        raise HTTPException(status_code=404, detail=f"Comment item with id {id} not found")

    # Update the attributes of the existing_comment with the values from the comment parameter
    existing_comment.parent_id = comment.parent_id
    existing_comment.post_id = comment.post_id
    existing_comment.user_id = comment.user_id
    existing_comment.content = comment.content

    session.commit()
    session.refresh(existing_comment)

    return existing_comment

    return existing_comment

#delete comment by id
def delete_comment(session: Session, id: int):
    # get the given id
    comment = session.query(models.CommentModel.Comment).get(id)
 
    # if comment item with given id exists, delete it from the database. Otherwise raise 404 error
    if comment:
        session.delete(comment)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"comment item with id {id} not found")

    return {"message": f"comment item with id {id} is deleted successful"}