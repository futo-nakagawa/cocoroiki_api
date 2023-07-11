from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from Family import schema as familyschema
from AppUser import schema as userschema

# =================================Relation===========================================
# Create Relation Schema (Pydantic Model)
class RelationCreate(BaseModel):
    user_id: int = None
    family_id: int = None

# Complete Relation Schema (Pydantic Model)
class Relation(BaseModel):
    id: int
    user_id: int
    user: userschema.AppUser = None
    family_id: int
    family: familyschema.Family = None

    class Config:
        orm_mode = True
