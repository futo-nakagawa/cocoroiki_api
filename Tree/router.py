from typing import List
from fastapi import status, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from Tree import controller
import schemas
from src.config import get_session

router = APIRouter()

# ===============================Tree=============================================
@router.get("/trees", response_model = List[schemas.TreeSchema.Tree], tags=["trees"])
def 木一覧取得(session: Session = Depends(get_session)):
    alltree = controller.get_tree(session)
    return alltree

@router.get("/trees/{id}", response_model=schemas.TreeSchema.Tree, tags=["trees"])
def 特定の木の取得(id: int, session: Session = Depends(get_session)):
    treebyID = controller.get_tree_by_id(session, id=id)
    return treebyID

     
@router.post("/trees", response_model=schemas.TreeSchema.Tree, status_code=status.HTTP_201_CREATED, tags=["trees"])
def 木の作成(tree: schemas.TreeSchema.TreeCreate, session: Session = Depends(get_session)):
    createtree = controller.create_tree(session, tree=tree)
    return createtree 

 
@router.put("/trees/{id}", response_model=schemas.TreeSchema.Tree, tags=["trees"])
def 特定の木の更新(id: int, tree: schemas.TreeSchema.TreeCreate, session: Session = Depends(get_session)):
    updatetree =controller.update_tree(session, tree=tree, id=id)
    return updatetree
 
@router.delete("/trees/{id}", tags=["trees"])
def 特定の木の削除(id: int, session: Session = Depends(get_session)):
    deletetree = controller.delete_tree(session, id=id)
    return deletetree