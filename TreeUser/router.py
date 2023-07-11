from typing import List
from fastapi import status, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from TreeUser import controller
import schemas
from src.config import get_session

router = APIRouter()

# ===============================TreeUser=============================================
@router.get("/tree_users", response_model = List[schemas.TreeUserSchema.TreeUser], tags=["tree_users"])
def 木とユーザーの一覧取得(session: Session = Depends(get_session)):
    alltree_user = controller.get_tree_user(session)
    return alltree_user

@router.get("/tree_users/{id}", response_model=schemas.TreeUserSchema.TreeUser, tags=["tree_users"])
def 特定の木とユーザーの取得(id: int, session: Session = Depends(get_session)):
    tree_userbyID = controller.get_tree_user_by_id(session, id=id)
    return tree_userbyID
    
@router.post("/tree_users", response_model=schemas.TreeUserSchema.TreeUser, status_code=status.HTTP_201_CREATED, tags=["tree_users"])
def 木とユーザーの作成(tree_user: schemas.TreeUserSchema.TreeUserCreate, session: Session = Depends(get_session)):
    createtree_user = controller.create_tree_user(session, tree_user=tree_user)
    return createtree_user 
 
@router.put("/tree_users/{id}", response_model=schemas.TreeUserSchema.TreeUser, tags=["tree_users"])
def 特定の木とユーザーの更新(id: int, tree_user: schemas.TreeUserSchema.TreeUserCreate, session: Session = Depends(get_session)):
    updatetree_user =controller.update_tree_user(session, tree_user=tree_user, id=id)
    return updatetree_user
 
@router.delete("/tree_users/{id}", tags=["tree_users"])
def 特定の木とユーザーの削除(id: int, session: Session = Depends(get_session)):
    deletetree_user = controller.delete_tree_user(session, id=id)
    return deletetree_user