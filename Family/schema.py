from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# =================================Family===========================================
# Create Family Schema (Pydantic Model)
class FamilyCreate(BaseModel):
    name: str
    total: int

# Complete Family Schema (Pydantic Model)
class Family(BaseModel):
    id: int
    name: str
    total: int
    createdAt: datetime = None
    updatedAt: datetime = None

    class Config:
        orm_mode = True
