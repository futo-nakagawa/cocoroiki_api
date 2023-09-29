from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from database import Base

# AppUser
class AppUser(Base):
    __tablename__ = 'app_users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    birth = Column(Integer)
    age = Column(Integer)
    gender = Column(String)
    # quest_role = Column(Boolean)
    # family_id = Column(Integer, ForeignKey('Families.id'))
    grandparent = Column(Boolean)
    last_login = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    published_at = Column(DateTime)

    # family = relationship("Family", back_populates="user")
    # post = relationship("Post", back_populates="user")
    # relation = relationship("Relation", back_populates="user")
    # comment = relationship("Comment", back_populates="user")
    # tree_user = relationship("TreeUser", back_populates="user")