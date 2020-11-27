import praw

reddit = praw.Reddit(
    client_id='uPfZe_DBd33CNQ',
    client_secret='agUDFRuHKtARBlwR_w0QQ385PLwZSw',
    user_agent='linux:reddit4nlp:v0 (by /u/lilinformatiker)',
)



def retrieve_top_posts_from_subreddits(subreddits, limit=300):
    for subreddit in subreddits:
        for submission in reddit.subreddit(subreddit).top(limit=limit):
            f = open(f'data/post_data/{subreddit}/{submission.id}.txt', "x")

            if not submission.selftext:
                print('no selftext')
                
            f.write(submission.selftext)
            f.close()

    


if __name__ == "__main__":
    subreddits = [
        'learnpython',
    ]

    retrieve_top_posts_from_subreddits(subreddits)