from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from Family import schema as schema

# =================================App_User=========================================== 
# Create appUser Schema (Pydantic Model)
class AppUserCreate(BaseModel):
    name: str
    email: str
    password: str
    birth: int
    age: int
    gender: str
    quest_role: bool
    family_id: int = None
    grandparent: bool

# Complete appUser Schema (Pydantic Model)
class AppUser(BaseModel):
    id: int
    name: str = None
    email: str = None
    password: str = None
    birth: int = None
    age: int = None
    gender: str = None
    # quest_role: bool 
    # family_id: int
    # family: schema.Family = None
    grandparent: bool
    last_login: datetime = None
    created_at: datetime = None
    updated_at: datetime = None
    published_at: datetime = None

    class Config:
        orm_mode = True
