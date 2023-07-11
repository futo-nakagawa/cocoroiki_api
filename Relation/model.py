from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from database import Base

# Relation
class Relation(Base):
    __tablename__ = 'Relations'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    family_id = Column(Integer, ForeignKey('Families.id'))

    family = relationship("Family", back_populates="relation")
    user = relationship("AppUser", back_populates="relation")