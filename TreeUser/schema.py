from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from Tree import schema as treeschema
from AppUser import schema as userschema

# =================================TreeUser===========================================
# Create TreeUser Schema (Pydantic Model)
class TreeUserCreate(BaseModel):
    tree_id: int = None
    user_id: int = None

# Complete TreeUser Schema (Pydantic Model)
class TreeUser(BaseModel):
    id: int
    tree_id: int
    tree: treeschema.Tree = None
    user_id: int
    user: userschema.AppUser = None

    class Config:
        orm_mode = True
