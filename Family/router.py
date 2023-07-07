from typing import List
from fastapi import status, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from Family import controller
import schemas
from src.config import get_session

router = APIRouter()

# ===============================Family=============================================
@router.get("/families", response_model = List[schemas.FamilySchema.Family], tags=["families 家族"])
def 家族一覧取得(session: Session = Depends(get_session)):
    allfamily = controller.get_family(session)
    return allfamily


@router.get("/families/{id}", response_model=schemas.FamilySchema.Family, tags=["families 家族"])
def 特定の家族の取得(id: int, session: Session = Depends(get_session)):
    familybyID = controller.get_family_by_id(session, id=id)
    return familybyID

 
@router.post("/families", response_model=schemas.FamilySchema.Family, status_code=status.HTTP_201_CREATED, tags=["families 家族"])
def 家族の作成(family: schemas.FamilySchema.FamilyCreate, session: Session = Depends(get_session)):
    createfamily = controller.create_family(session, family=family)
    return createfamily 

 
@router.put("/families/{id}", response_model=schemas.FamilySchema.Family, tags=["families 家族"])
def 特定の家族の更新(id: int, family: schemas.FamilySchema.FamilyCreate, session: Session = Depends(get_session)):
    updatefamily =controller.update_family(session, family=family, id=id)
    return updatefamily
 
@router.delete("/families/{id}", tags=["families 家族"])
def 特定の家族の削除(id: int, session: Session = Depends(get_session)):
    deletefamily = controller.delete_family(session, id=id)
    return deletefamily