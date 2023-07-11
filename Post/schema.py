from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from AppUser import schema as schema

# =================================Post===========================================
# Create Post Schema (Pydantic Model)
class PostCreate(BaseModel):
    user_id: int = None
    kids: int
    content: str
    image_url: str
    like: int

# Complete Post Schema (Pydantic Model)
class Post(BaseModel):
    id: int
    user_id: int
    user: schema.AppUser = None
    kids: int
    content: str
    image_url: str
    like: int
    createdAt: datetime = None
    updatedAt: datetime = None
    publishedAt: datetime = None

    class Config:
        orm_mode = True
