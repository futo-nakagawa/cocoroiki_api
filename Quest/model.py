from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from database import Base

# Quest
class Quest(Base):
    __tablename__ = 'Quests'

    id = Column(Integer, primary_key=True)
    content = Column(Integer)
    quest_kinds = Column(Integer, ForeignKey('QuestTypes.id'))
    completed = Column(Boolean)

    quests = relationship("QuestType", back_populates="quest_id")
 