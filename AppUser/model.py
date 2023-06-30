from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from database import Base

# AppUser
class AppUser(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    birth = Column(Integer)
    age = Column(Integer)
    gender = Column(String)
    quest_role = Column(Boolean)
    family_id = Column(Integer, ForeignKey('Families.id'))
    last_login = Column(DateTime)
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    publishedAt = Column(DateTime)

    family = relationship("Family", back_populates="user")
    post = relationship("Post", back_populates="user")