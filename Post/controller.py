from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
import models, schemas

#get all post
def get_post(session: Session):
    post_list = session.query(models.PostModel.Post).all() # get all post items 
    return post_list 

#get post by id
def get_post_by_id(session: Session, id: int):
    post = session.query(models.PostModel.Post).get(id) # get item with the given id
 
    # check if id exists. If not, return 404 not found response
    if not post:
        raise HTTPException(status_code=404, detail=f"post item with id {id} not found")
 
    return post

#create post
def create_post(session: Session, post: schemas.PostSchema.PostCreate):
    postdb = models.PostModel.Post(
        user_id=post.user_id,
        kids=post.kids,
        content=post.content,
        image_url=post.image_url,
        like=post.like,
        createdAt=datetime.today(),
        updatedAt=datetime.today(),
        publishedAt=datetime.today()
    )
 
    session.add(postdb)
    session.commit()
    session.refresh(postdb)
 
    return postdb

#update post by id
def update_post(session: Session, post: schemas.PostSchema.PostCreate, id: int):
    # Check if the post item with the given id exists
    existing_post = session.query(models.PostModel.Post).get(id)
    if not existing_post:
        raise HTTPException(status_code=404, detail=f"Post item with id {id} not found")

    # Update the attributes of the existing_post with the values from the post parameter
    existing_post.user_id = post.user_id
    existing_post.kids = post.kids
    existing_post.content = post.content
    existing_post.image_url = post.image_url
    existing_post.like = post.like

    session.commit()
    session.refresh(existing_post)

    return existing_post

#delete post by id
def delete_post(session: Session, id: int):
    # get the given id
    post = session.query(models.PostModel.Post).get(id)
 
    # if post item with given id exists, delete it from the database. Otherwise raise 404 error
    if post:
        session.delete(post)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"post item with id {id} not found")

    return {"message": f"post item with id {id} is deleted successful"}