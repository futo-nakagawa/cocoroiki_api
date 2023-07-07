from typing import List
from fastapi import status, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from QuestType import controller
import schemas
from src.config import get_session

router = APIRouter()

# ===============================QuestType=============================================
@router.get("/quest_types", response_model = List[schemas.QuestTypeSchema.QuestType], tags=["quest_types"])
def クエストタイプ一覧取得(session: Session = Depends(get_session)):
    allquest_type = controller.get_quest_type(session)
    return allquest_type

@router.get("/quest_types/{id}", response_model=schemas.QuestTypeSchema.QuestType, tags=["quest_types"])
def 特定のクエストタイプの取得(id: int, session: Session = Depends(get_session)):
    quest_typebyID = controller.get_quest_type_by_id(session, id=id)
    return quest_typebyID
    
@router.post("/quest_types", response_model=schemas.QuestTypeSchema.QuestType, status_code=status.HTTP_201_CREATED, tags=["quest_types"])
def クエストタイプの作成(questtype: schemas.QuestTypeSchema.QuestTypeCreate, session: Session = Depends(get_session)):
    createquest_type = controller.create_quest_type(session, questtype=questtype)
    return createquest_type 
 
@router.put("/quest_types/{id}", response_model=schemas.QuestTypeSchema.QuestType, tags=["quest_types"])
def 特定のクエストタイプの更新(id: int, questtype: schemas.QuestTypeSchema.QuestTypeCreate, session: Session = Depends(get_session)):
    updatequest_type =controller.update_quest_type(session, questtype=questtype, id=id)
    return updatequest_type
 
@router.delete("/quest_types/{id}", tags=["quest_types"])
def 特定のクエストタイプの削除(id: int, session: Session = Depends(get_session)):
    deletequest_type = controller.delete_quest_type(session, id=id)
    return deletequest_type