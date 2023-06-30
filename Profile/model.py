from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from database import Base

# Profile
class Profile(Base):
    __tablename__ = 'Profiles'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    image = Column(String)
    content = Column(String)
