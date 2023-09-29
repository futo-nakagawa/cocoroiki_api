from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from database import Base

# Comment
class Comment(Base):
    __tablename__ = 'Comments'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer)
    post_id = Column(Integer, ForeignKey('Posts.id'))
    user_id = Column(Integer, ForeignKey('Users.id'))
    content = Column(String)
    createdAt = Column(DateTime)

    # post = relationship("Post", back_populates="comment")
    # user = relationship("AppUser", back_populates="comment")