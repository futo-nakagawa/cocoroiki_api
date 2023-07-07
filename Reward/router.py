from typing import List
from fastapi import status, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from Reward import controller
import schemas
from src.config import get_session

router = APIRouter()

# ===============================Reward=============================================
@router.get("/rewards", response_model = List[schemas.RewardSchema.Reward], tags=["rewards"])
def 褒美一覧取得(session: Session = Depends(get_session)):
    allreward = controller.get_reward(session)
    return allreward

@router.get("/rewards/{id}", response_model=schemas.RewardSchema.Reward, tags=["rewards"])
def 特定の褒美の取得(id: int, session: Session = Depends(get_session)):
    rewardbyID = controller.get_reward_by_id(session, id=id)
    return rewardbyID
 
@router.post("/rewards", response_model=schemas.RewardSchema.Reward, status_code=status.HTTP_201_CREATED, tags=["rewards"])
def 褒美の作成(reward: schemas.RewardSchema.RewardCreate, session: Session = Depends(get_session)):
    createreward = controller.create_reward(session, reward=reward)
    return createreward 
 
@router.put("/rewards/{id}", response_model=schemas.RewardSchema.Reward, tags=["rewards"])
def 特定の褒美の更新(id: int, reward: schemas.RewardSchema.RewardCreate, session: Session = Depends(get_session)):
    updatereward =controller.update_reward(session, reward=reward, id=id)
    return updatereward

@router.delete("/rewards/{id}", tags=["rewards"])
def 特定の褒美の削除(id: int, session: Session = Depends(get_session)):
    deletereward = controller.delete_reward(session, id=id)
    return deletereward