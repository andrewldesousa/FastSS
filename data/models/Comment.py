from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from data.db import Base, engine


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    body = Column(String)
    author = Column(String) 
    upvotes = Column(Integer)
    downvotes = Column(Integer)

    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("Post", back_populates="comments")