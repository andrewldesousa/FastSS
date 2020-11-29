import praw
import os
import sqlite3

reddit = praw.Reddit(
    client_id='uPfZe_DBd33CNQ',
    client_secret='agUDFRuHKtARBlwR_w0QQ385PLwZSw',
    user_agent='linux:reddit4nlp:v0 (by /u/lilinformatiker)',
)
sql_transaction = []
databasePath = 'C:/Users/USER/Desktop/NLP-SEMINAR0511/subredditPosts.db'
conn = sqlite3.connect(databasePath)
c = conn.cursor()



def perform_executions():
    global sql_transaction
    # retry_transaction = []
    success = 0
    fail = 0
    #print(sql_transaction)
   
    former_len = len(sql_transaction)
    print("Inserting Queries into database")
    c.execute('BEGIN TRANSACTION')
    for s in sql_transaction:
        try:
            c.execute(s)
            success += 1
        except Exception as e:
            # retry_transaction.append(s)
            fail += 1
            print("could not execute SQL: ", s)
            print("ERROR: ", e)
            pass
    conn.commit()
    sql_transaction = []
    
    print("Operation details: Total - {} Fail - {} |  Success - {}".format(former_len, fail, success))


def acceptable_data(data):
    if len(data.split(' ')) > 50 or len(data) < 1:
        return False
    #elif len(data) > 500:
    #    return False
    
    else:
        return True
def transaction_bldr(sql):
    global sql_transaction
    sql_transaction.append(sql)

    if len(sql_transaction) >= 100:
        perform_executions()
        
def create_table():
    sql = "CREATE TABLE IF NOT EXISTS subreddit_posts(post_id TEXT,post_name TEXT,post TEXT, comment_length INT, ups INT)"
    c.execute(sql)
    

def format_data(data):
    data = data.replace("\n", " newlinechar ").replace("\r", " newlinechar ").replace('"', "'").replace("\t", " newlinechar ")
    return data
  


def sql_insert_has_parent(post_id,pname, submission,comment_length, ups):
   
    try:
        sql = """INSERT INTO subreddit_posts(post_id,post_name,post, comment_length, ups) VALUES ("{}","{}","{}","{}","{}");""".format(
            post_id,pname, submission,comment_length, ups)

        transaction_bldr(sql)
        
    except Exception as e:
        print('Insertion0 error: ', str(e))
    

#submission id    
#submission name
#submission text
#submission length of comments
#submission ups


 


if __name__ == "__main__":
    
    subreddits = [
        'learnpython',
        'AskReddit',
        'politics',
        'PS5',
        'funny',
        'wow'
    ]
    #subreddits= reddit.subreddits.popular(limit=10)
    #print(sub)
    #subreddits =list(reddit.subreddits(limit=None))
    #print("We are working on these subreddits:")
    #for s in subreddits:
    #    print(s)
    create_table()
    for sub in subreddits:
        #os.mkdir(f'./data/{subreddit}')
        print(f"Working on {sub}")
        for submission in reddit.subreddit(sub).top(limit=300):
            
            #f = open(f'./data/{subreddit}/{submission.id}.txt', "x")
            #print(f"Submission text      {submission.selftext}")
            if submission.selftext!=' ':
                if acceptable_data(submission.selftext):
                    #print('no selftext')
                    data = format_data(submission.selftext)
                    #print(len(submission.comments))
                    sql_insert_has_parent(submission.id,sub,data,len(submission.comments),submission.ups)       
                    #f.write(submission.selftext)
                    #f.close()
    if sql_transaction!=[]:
        perform_executions()