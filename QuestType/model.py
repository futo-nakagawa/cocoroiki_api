from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from database import Base

# Quest types
class QuestType(Base):
    __tablename__ = 'QuestTypes'

    id = Column(Integer, primary_key=True)
    kinds = Column(String)
    online = Column(Boolean)

    quest_id = relationship("Quest", back_populates="quests")
