import praw

reddit = praw.Reddit(
    client_id='uPfZe_DBd33CNQ',
    client_secret='agUDFRuHKtARBlwR_w0QQ385PLwZSw',
    user_agent='linux:reddit4nlp:v0 (by /u/lilinformatiker)',
)

for submission in reddit.subreddit("learnpython").hot(limit=10):
    print(submission.title)


if __name__ == "__main__":
    print(reddit.read_only)