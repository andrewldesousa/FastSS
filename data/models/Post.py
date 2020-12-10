import praw
from sqlalchemy import Table, Column, Integer, Float, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from data.db import Base, engine, reddit
from .Comment import Comment


class Post(Base):
    __tablename__ = 'post'
    id = Column(String, primary_key=True)
    title = Column(String)
    body = Column(String)
    author_name = Column(String) 
    score = Column(Integer)
    upvote_ratio = Column(Float)
    has_full_body = Column(Boolean)
    subreddit = Column(String) 

    comments = relationship("Comment", back_populates="post")

    def __init__(self, praw_post):
        self.id = praw_post.id
        self.title = praw_post.title
        self.body = praw_post.selftext
        self.author_name = praw_post.author.name if praw_post.author else None
        self.score = praw_post.score
        self.upvote_ratio = praw_post.upvote_ratio
        self.has_full_body = False
        self.subreddit = praw_post.subreddit.name

        comments = []
        for i in list(praw_post.comments):
            if isinstance(i, praw.models.Comment):
                comments.append(Comment(praw_post, i))
            else:
                break
        self.comments = comments