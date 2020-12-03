from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from data.db import Base, engine


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(String, primary_key=True)
    body = Column(String)
    author_name = Column(String) 
    score = Column(Integer)

    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("Post", back_populates="comments")

    def __init__(self, praw_post, praw_comment):
        self.id = praw_comment.id
        self.body = praw_comment.body
        self.author_name = praw_comment.author.name if praw_comment.author else None
        self.score = praw_comment.score
        self.post_id = praw_post.id