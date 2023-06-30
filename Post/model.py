from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from database import Base

# Post
class Post(Base):
    __tablename__ = 'Posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    kids = Column(Integer)
    content = Column(String)
    image_url = Column(String)
    like = Column(Integer)
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    publishedAt = Column(DateTime)

    user = relationship("AppUser", back_populates="post")
