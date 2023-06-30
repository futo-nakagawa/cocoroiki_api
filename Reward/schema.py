from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# =================================Rewards===========================================
# Create Reward Schema (Pydantic Model)
class RewardCreate(BaseModel):
    content: str

# Complete Reward Schema (Pydantic Model)
class Reward(BaseModel):
    id: int
    content: str

    class Config:
        orm_mode = True
