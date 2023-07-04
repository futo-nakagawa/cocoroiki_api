from typing import List
from fastapi import status, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from Profile import controller
import schemas
from src.config import get_session

router = APIRouter()

# # ===============================Profile=============================================
@router.get("/profiles", response_model = List[schemas.ProfileSchema.Profile], tags=["profiles プロファイル"])
def プロファイル一覧取得(session: Session = Depends(get_session)):
    allprofile =  controller.get_profile(session)
    return allprofile

@router.get("/profiles/{id}", response_model=schemas.ProfileSchema.Profile, tags=["profiles プロファイル"])
def 特定のプロファイルの取得(id: int, session: Session = Depends(get_session)):
    profilebyID =  controller.get_profile_by_id(session, id=id)
    return profilebyID

@router.post("/profiles", response_model=schemas.ProfileSchema.Profile, status_code=status.HTTP_201_CREATED, tags=["profiles プロファイル"])
def プロファイルの作成(profile: schemas.ProfileSchema.ProfileCreate, session: Session = Depends(get_session)):
    createprofile =  controller.create_profile(session, profile=profile)
    return createprofile 
 
@router.put("/profiles/{id}", response_model=schemas.ProfileSchema.Profile, tags=["profiles プロファイル"])
def 特定のプロファイルの更新(id: int, profile: schemas.ProfileSchema.ProfileCreate, session: Session = Depends(get_session)):
    updateprofile = controller.update_profile(session, profile=profile, id=id)
    return updateprofile
 
@router.delete("/profiles/{id}", tags=["profiles プロファイル"])
def 特定のプロファイルの削除(id: int, session: Session = Depends(get_session)):
    deleteprofile =  controller.delete_profile(session, id=id)
    return deleteprofile