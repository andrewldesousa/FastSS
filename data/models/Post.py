
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from data.db import Base, engine


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
    author = Column(String) 
    upvotes = Column(Integer)
    downvotes = Column(Integer)
    comments = relationship("Comment", back_populates="post")


    def __init__(self, praw_post):
        self.body = praw_post.selftext
        # self.body = Column(String)
        # self.author = praw_post.author
        # self.upvotes = praw_post.upvotes
        # self.comments = praw_post.