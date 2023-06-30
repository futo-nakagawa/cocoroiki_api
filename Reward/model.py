from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from database import Base

# Rewards
class Reward(Base):
    __tablename__ = 'Rewards'

    id = Column(Integer, primary_key=True)
    content = Column(String)
