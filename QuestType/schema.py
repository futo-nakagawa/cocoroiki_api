from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# =================================QuestType===========================================
# Create QuestType Schema (Pydantic Model)
class QuestTypeCreate(BaseModel):
    kinds: str
    online: bool

# Complete QuestType Schema (Pydantic Model)
class QuestType(BaseModel):
    id: int
    kinds: str
    online: bool

    class Config:
        orm_mode = True
