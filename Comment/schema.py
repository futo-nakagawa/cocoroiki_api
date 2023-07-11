from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from Post import schema as postschema
from AppUser import schema as userschema

# =================================Comment===========================================
# Create Comment Schema (Pydantic Model)
class CommentCreate(BaseModel):
    parent_id: int
    post_id: int = None
    user_id: int = None
    content: str

# Complete Comment Schema (Pydantic Model)
class Comment(BaseModel):
    id: int
    parent_id: int
    post_id: int
    post: postschema.Post = None
    user_id: int
    user: userschema.AppUser = None
    content: str
    createdAt: datetime = None
    
    class Config:
        orm_mode = True
