from typing import List
from fastapi import status, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from Closeness import controller
import schemas
from src.config import get_session

router = APIRouter()

# ===============================Closeness=============================================
@router.get("/closeness", response_model = List[schemas.ClosenessSchema.Closeness], tags=["closeness"])
def Closenessの一覧取得(session: Session = Depends(get_session)):
    allcloseness = controller.get_closeness(session)
    return allcloseness

@router.get("/closeness/{id}", response_model=schemas.ClosenessSchema.Closeness, tags=["closeness"])
def 特定のClosenessを取得(id: int, session: Session = Depends(get_session)):
    closenessbyID = controller.get_closeness_by_id(session, id=id)
    return closenessbyID
 
@router.post("/closeness", response_model=schemas.ClosenessSchema.Closeness, status_code=status.HTTP_201_CREATED, tags=["closeness"])
def Closenessの作成(closeness: schemas.ClosenessSchema.ClosenessCreate, session: Session = Depends(get_session)):
    createcloseness = controller.create_closeness(session, closeness=closeness)
    return createcloseness 
 
@router.put("/closeness/{id}", response_model=schemas.ClosenessSchema.Closeness, tags=["closeness"])
def 特定のClosenessの更新(id: int, closeness: schemas.ClosenessSchema.ClosenessCreate, session: Session = Depends(get_session)):
    updatecloseness =controller.update_closeness(session, closeness=closeness, id=id)
    return updatecloseness
 
@router.delete("/closeness/{id}", tags=["closeness"])
def 特定のClosenessの削除(id: int, session: Session = Depends(get_session)):
    deletecloseness = controller.delete_closeness(session, id=id)
    return deletecloseness