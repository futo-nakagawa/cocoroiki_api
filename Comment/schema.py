from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
        
# =================================Comment===========================================
# Create Comment Schema (Pydantic Model)
class CommentCreate(BaseModel):
    parent_id: int
    post_id: int
    user_id: int
    content: str

# Complete Comment Schema (Pydantic Model)
class Comment(BaseModel):
    id: int
    parent_id: int
    post_id: int
    user_id: int
    content: str
    createdAt: datetime = None
    
    class Config:
        orm_mode = True
