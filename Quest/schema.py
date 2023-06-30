from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from QuestType import schema as schema

# =================================Quest===========================================
# Create Quest Schema (Pydantic Model)
class QuestCreate(BaseModel):
    content: int
    quest_kinds: int
    completed: bool

# Complete Quest Schema (Pydantic Model)
class Quest(BaseModel):
    id: int
    content: int
    quest_kinds: int
    quests: schema.QuestType
    completed: bool

    class Config:
        orm_mode = True
