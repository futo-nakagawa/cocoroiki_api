from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# =================================Closeness===========================================
# Create Quest Schema (Pydantic Model)
class ClosenessCreate(BaseModel):
    tree_id: int
    close_meter: int

# Complete Quest Schema (Pydantic Model)
class Closeness(BaseModel):
    id: int
    tree_id: int
    close_meter: int

    class Config:
        orm_mode = True
