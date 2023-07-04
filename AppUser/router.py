from typing import List
from fastapi import status, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from AppUser import controller
import schemas
from src.config import get_session

router = APIRouter()

# ===============================AppUser=============================================
@router.get("/app-users", response_model = List[schemas.AppUserSchema.AppUser], tags=["users ユーザー"])
def ユーザー一覧取得(session: Session = Depends(get_session)): 
    alluser = controller.get_user(session)
    return alluser

@router.get("/app-users/{id}", response_model=schemas.AppUserSchema.AppUser, tags=["users ユーザー"])
def 特定のユーザーの取得(id: int, session: Session = Depends(get_session)):
    userbyID = controller.get_user_by_id(session, id=id)
    return userbyID
 
@router.post("/app-users", response_model=schemas.AppUserSchema.AppUser, status_code=status.HTTP_201_CREATED, tags=["users ユーザー"])
def ユーザーの作成(users: schemas.AppUserSchema.AppUserCreate, session: Session = Depends(get_session)):
    createuser = controller.create_user(session, users=users)
    return createuser 
 
@router.put("/app-users/{id}", response_model=schemas.AppUserSchema.AppUser, tags=["users ユーザー"])
def 特定のユーザーの更新(id: int, users: schemas.AppUserSchema.AppUserCreate, session: Session = Depends(get_session)):
    updateuser =controller.update_user(session, users=users, id=id)
    return updateuser
 
@router.delete("/app-users/{id}", tags=["users ユーザー"])
def 特定のユーザーの削除(id: int, session: Session = Depends(get_session)):
    deleteuser = controller.delete_user(session, id=id)
    return deleteuser
