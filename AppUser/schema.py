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
    family_id: int

# Complete appUser Schema (Pydantic Model)
class AppUser(BaseModel):
    id: int
    name: str
    email: str
    password: str
    birth: int
    age: int
    gender: str
    quest_role: bool
    family_id: int
    family: schema.Family
    last_login: datetime = None
    createdAt: datetime = None
    updatedAt: datetime = None
    publishedAt: datetime = None

    class Config:
        orm_mode = True
