from typing import List
from fastapi import status, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from Comment import controller
import schemas
from src.config import get_session

router = APIRouter()

# ===============================Comment=============================================
@router.get("/comments", response_model = List[schemas.CommentSchema.Comment], tags=["comments"])
def コメント一覧取得(session: Session = Depends(get_session)):
    allcomment = controller.get_comment(session)
    return allcomment

@router.get("/comments/{id}", response_model=schemas.CommentSchema.Comment, tags=["comments"])
def 特定のコメントの取得(id: int, session: Session = Depends(get_session)):
    commentbyID = controller.get_comment_by_id(session, id=id)
    return commentbyID

     
@router.post("/comments", response_model=schemas.CommentSchema.Comment, status_code=status.HTTP_201_CREATED, tags=["comments"])
def コメントの作成(comment: schemas.CommentSchema.CommentCreate, session: Session = Depends(get_session)):
    createcomment = controller.create_comment(session, comment=comment)
    return createcomment 

 
@router.put("/comments/{id}", response_model=schemas.CommentSchema.Comment, tags=["comments"])
def 特定のコメントの更新(id: int, comment: schemas.CommentSchema.CommentCreate, session: Session = Depends(get_session)):
    updatecomment =controller.update_comment(session, comment=comment, id=id)
    return updatecomment
 
@router.delete("/comments/{id}", tags=["comments"])
def 特定のコメントの削除(id: int, session: Session = Depends(get_session)):
    deletecomment = controller.delete_comment(session, id=id)
    return deletecomment