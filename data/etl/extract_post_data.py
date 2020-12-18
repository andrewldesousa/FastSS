import sys
sys.path.append('.')


from data.models import Post, Comment
from data.db import Base, engine, Session, reddit
from data.Subreddit import Subreddits


def extract_posts_and_comments():
    Base.metadata.create_all(engine)
    session = Session()
    limit = 2000

    for subreddit in Subreddits.list_subreddits():
        print(f'Extracting {subreddit} data...')
        i = 0
        for submission in reddit.subreddit(subreddit).top(limit=limit):
            i+=1
            print(f'Processing post {i} out of {limit}.')
            p = Post(submission, add_comments=False) # adding comments is slow
            session.add(p)
    session.commit()

if __name__ == '__main__':
    extract_posts_and_comments()