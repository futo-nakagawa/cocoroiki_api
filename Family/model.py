from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from database import Base

# Families
class Family(Base):
    __tablename__ = 'Families'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    total = Column(Integer)
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)

    # user = relationship("AppUser", back_populates="family")
    # relation = relationship("Relation", back_populates="family")