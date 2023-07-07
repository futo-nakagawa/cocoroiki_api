from typing import List
from fastapi import status, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from Quest import controller
import schemas
from src.config import get_session

router = APIRouter()

# ===============================Quest=============================================
@router.get("/quests", response_model = List[schemas.QuestSchema.Quest], tags=["quests"])
def クエスト一覧取得(session: Session = Depends(get_session)):
    allquest = controller.get_quest(session)
    return allquest

@router.get("/quests/{id}", response_model=schemas.QuestSchema.Quest, tags=["quests"])
def 特定のクエストの取得(id: int, session: Session = Depends(get_session)):
    questbyID = controller.get_quest_by_id(session, id=id)
    return questbyID
 
@router.post("/quests", response_model=schemas.QuestSchema.Quest, status_code=status.HTTP_201_CREATED, tags=["quests"])
def クエストの作成(quests: schemas.QuestSchema.QuestCreate, session: Session = Depends(get_session)):
    createquest = controller.create_quest(session, quests=quests)
    return createquest 
 
@router.put("/quests/{id}", response_model=schemas.QuestSchema.Quest, tags=["quests"])
def 特定のクエストの更新(id: int, quests: schemas.QuestSchema.QuestCreate, session: Session = Depends(get_session)):
    updatequest =controller.update_quest(session, quests=quests, id=id)
    return updatequest
 
@router.delete("/quests/{id}", tags=["quests"])
def 特定のクエストの削除(id: int, session: Session = Depends(get_session)):
    deletequest = controller.delete_quest(session, id=id)
    return deletequest