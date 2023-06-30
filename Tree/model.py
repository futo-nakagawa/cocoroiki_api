from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from database import Base

# Tree
class Tree(Base):
    __tablename__ = 'Trees'

    id = Column(Integer, primary_key=True)
    growth_stage = Column(Integer)
    quest = Column(Integer)
    watering = Column(DateTime)

    closeness = relationship("Closeness", back_populates="tree")
