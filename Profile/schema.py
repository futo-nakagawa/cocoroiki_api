from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# =================================Profile===========================================
# Create Profile Schema (Pydantic Model)
class ProfileCreate(BaseModel):
    name: str
    image: str
    content: str

# Complete Profile Schema (Pydantic Model)
class Profile(BaseModel):
    id: int
    name: str
    image: str
    content: str
 
    class Config:
        orm_mode = True
