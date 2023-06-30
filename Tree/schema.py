from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# =================================Tree===========================================
# Create Tree Schema (Pydantic Model)
class TreeCreate(BaseModel):
    growth_stage: int
    quest: int

# Complete Tree Schema (Pydantic Model)
class Tree(BaseModel):
    id: int
    growth_stage: int
    quest: int
    watering: datetime = None

    class Config:
        orm_mode = True
