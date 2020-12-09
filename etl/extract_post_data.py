import sys
sys.path.append('.')

import praw
from data.models import Post, Comment
from data.db import Base, engine, Session
from data.Subreddit import Subreddits

reddit = praw.Reddit(
    client_id='uPfZe_DBd33CNQ',
    client_secret='agUDFRuHKtARBlwR_w0QQ385PLwZSw',
    user_agent='linux:reddit4nlp:v0 (by /u/lilinformatiker)',
)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = Session()
    limit = 5000

    for subreddit in Subreddits.list_subreddits():
        print(f'Extracting {subreddit} data...')
        for submission in reddit.subreddit(subreddit).top(limit=limit):
            p = Post(submission)
            session.add(p)
    session.commit()