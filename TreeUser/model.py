from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from database import Base

# TreeUser
class TreeUser(Base):
    __tablename__ = 'TreeUsers'

    id = Column(Integer, primary_key=True)
    tree_id = Column(Integer, ForeignKey('Trees.id'))
    user_id = Column(Integer, ForeignKey('Users.id'))

    # tree = relationship("Tree", back_populates="tree_user")
    # user = relationship("AppUser", back_populates="tree_user")