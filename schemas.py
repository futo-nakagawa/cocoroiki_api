from pydantic import BaseModel
from datetime import datetime

# =================================App_User=========================================== 
# Create appUser Schema (Pydantic Model)
class AppUserCreate(BaseModel):
    name: str
    email: str
    password: str
    birth: int 
    age: int
    gender: str
    quest_role: bool
    family: str

# Complete appUser Schema (Pydantic Model)
class AppUser(BaseModel):
    id: int
    name: str
    email: str
    password: str
    birth: int 
    age: int
    gender: str
    quest_role: bool
    family: str
    last_login: datetime = None
    createdAt: datetime = None
    updatedAt: datetime = None
    publishedAt: datetime = None
 
    class Config:
        orm_mode = True

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

# =================================Family===========================================
# Create Family Schema (Pydantic Model)
class FamilyCreate(BaseModel):
    name: str

# Complete Family Schema (Pydantic Model)
class Family(BaseModel):
    id: int
    name: str
    createdAt: datetime = None
    updatedAt: datetime = None

    class Config:
        orm_mode = True

# =================================Post===========================================
# Create Post Schema (Pydantic Model)
class PostCreate(BaseModel):
    user: int
    kids: int
    content: str
    image_url: str
    like: int

# Complete Post Schema (Pydantic Model)
class Post(BaseModel):
    id: int
    user: int
    kids: int
    content: str
    image_url: str
    like: int
    createdAt: datetime = None
    updatedAt: datetime = None
    publishedAt: datetime = None

    class Config:
        orm_mode = True
        
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


# =================================Quest===========================================
# Create Quest Schema (Pydantic Model)
class QuestCreate(BaseModel):
    content: int
    quest_kinds: str
    completed: bool

# Complete Quest Schema (Pydantic Model)
class Quest(BaseModel):
    id: int
    content: int
    quest_kinds: str
    completed: bool

    class Config:
        orm_mode = True




