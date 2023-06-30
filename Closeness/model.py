from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from database import Base
   
# Closeness
class Closeness(Base):
    __tablename__ = 'Closenesses'

    id = Column(Integer, primary_key=True)
    tree_id = Column(Integer, ForeignKey('Trees.id'))
    close_meter = Column(Integer)

    tree = relationship("Tree", back_populates="closeness")
