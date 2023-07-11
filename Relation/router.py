from typing import List
from fastapi import status, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from Relation import controller
import schemas
from src.config import get_session

router = APIRouter()

# ===============================Relation=============================================
@router.get("/relations", response_model = List[schemas.RelationSchema.Relation], tags=["relations"])
def クエストタイプ一覧取得(session: Session = Depends(get_session)):
    allrelation = controller.get_relation(session)
    return allrelation

@router.get("/relations/{id}", response_model=schemas.RelationSchema.Relation, tags=["relations"])
def 特定のクエストタイプの取得(id: int, session: Session = Depends(get_session)):
    relationbyID = controller.get_relation_by_id(session, id=id)
    return relationbyID
    
@router.post("/relations", response_model=schemas.RelationSchema.Relation, status_code=status.HTTP_201_CREATED, tags=["relations"])
def クエストタイプの作成(relation: schemas.RelationSchema.RelationCreate, session: Session = Depends(get_session)):
    createrelation = controller.create_relation(session, relation=relation)
    return createrelation 
 
@router.put("/relations/{id}", response_model=schemas.RelationSchema.Relation, tags=["relations"])
def 特定のクエストタイプの更新(id: int, relation: schemas.RelationSchema.RelationCreate, session: Session = Depends(get_session)):
    updaterelation =controller.update_relation(session, relation=relation, id=id)
    return updaterelation
 
@router.delete("/relations/{id}", tags=["relations"])
def 特定のクエストタイプの削除(id: int, session: Session = Depends(get_session)):
    deleterelation = controller.delete_relation(session, id=id)
    return deleterelation