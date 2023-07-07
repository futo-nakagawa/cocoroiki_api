from typing import List
from fastapi import status, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from Post import controller
import schemas
from src.config import get_session

router = APIRouter()

# ===============================Post=============================================
@router.get("/posts", response_model = List[schemas.PostSchema.Post], tags=["posts"])
def 投稿一覧取得(session: Session = Depends(get_session)):
    allpost = controller.get_post(session)
    return allpost

@router.get("/posts/{id}", response_model=schemas.PostSchema.Post, tags=["posts"])
def 特定の投稿の取得(id: int, session: Session = Depends(get_session)):
    postbyID = controller.get_post_by_id(session, id=id)
    return postbyID

 
@router.post("/posts", response_model=schemas.PostSchema.Post, status_code=status.HTTP_201_CREATED, tags=["posts"])
def 投稿の作成(post: schemas.PostSchema.PostCreate, session: Session = Depends(get_session)):
    createpost = controller.create_post(session, post=post)
    return createpost 
 
 
@router.put("/posts/{id}", response_model=schemas.PostSchema.Post, tags=["posts"])
def 特定の投稿の更新(id: int, post: schemas.PostSchema.PostCreate, session: Session = Depends(get_session)):
    updatepost =controller.update_post(session, post=post, id=id)
    return updatepost
 
@router.delete("/posts/{id}", tags=["posts"])
def 特定の投稿の削除(id: int, session: Session = Depends(get_session)):
    deletepost = controller.delete_post(session, id=id)
    return deletepost