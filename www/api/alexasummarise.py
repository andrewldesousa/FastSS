import praw
import os
import re
import time
import datetime
from praw.models import MoreComments

import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords 
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

from summarizer import Summarizer


reddit = praw.Reddit(
    client_id='uPfZe_DBd33CNQ',
    client_secret='agUDFRuHKtARBlwR_w0QQ385PLwZSw',
    user_agent='linux:reddit4nlp:v0 (by /u/lilinformatiker)',
)

data_dir='./'

def similar_posts(data1,data2):
  d1 = set(data1.split(" "))
  d2 = set(data2.split(" "))
  #print(d1)
  #print("---------------------------------------")
  #print(d2)
  intsct = d2.intersection(d1)
  if len(intsct)/max(len(d2),len(d1)) >=0.5:
    return True
  else:
    return False

def similar_to_doc(arr,data):
  for a in arr:
    if similar_posts(a,data):
      return True
  return False

contraction_mapping = {"ain't": "is not", "aren't": "are not","can't": "cannot", "'cause": "because", "could've": "could have", "couldn't": "could not",

                           "didn't": "did not", "doesn't": "does not", "don't": "do not", "hadn't": "had not", "hasn't": "has not", "haven't": "have not",

                           "he'd": "he would","he'll": "he will", "he's": "he is", "how'd": "how did", "how'd'y": "how do you", "how'll": "how will", "how's": "how is",

                           "I'd": "I would", "I'd've": "I would have", "I'll": "I will", "I'll've": "I will have","I'm": "I am", "I've": "I have", "i'd": "i would",

                           "i'd've": "i would have", "i'll": "i will",  "i'll've": "i will have","i'm": "i am", "i've": "i have", "isn't": "is not", "it'd": "it would",

                           "it'd've": "it would have", "it'll": "it will", "it'll've": "it will have","it's": "it is", "let's": "let us", "ma'am": "madam",

                           "mayn't": "may not", "might've": "might have","mightn't": "might not","mightn't've": "might not have", "must've": "must have",

                           "mustn't": "must not", "mustn't've": "must not have", "needn't": "need not", "needn't've": "need not have","o'clock": "of the clock",

                           "oughtn't": "ought not", "oughtn't've": "ought not have", "shan't": "shall not", "sha'n't": "shall not", "shan't've": "shall not have",

                           "she'd": "she would", "she'd've": "she would have", "she'll": "she will", "she'll've": "she will have", "she's": "she is",

                           "should've": "should have", "shouldn't": "should not", "shouldn't've": "should not have", "so've": "so have","so's": "so as",

                           "this's": "this is","that'd": "that would", "that'd've": "that would have", "that's": "that is", "there'd": "there would",

                           "there'd've": "there would have", "there's": "there is", "here's": "here is","they'd": "they would", "they'd've": "they would have",

                           "they'll": "they will", "they'll've": "they will have", "they're": "they are", "they've": "they have", "to've": "to have",

                           "wasn't": "was not", "we'd": "we would", "we'd've": "we would have", "we'll": "we will", "we'll've": "we will have", "we're": "we are",

                           "we've": "we have", "weren't": "were not", "what'll": "what will", "what'll've": "what will have", "what're": "what are",

                           "what's": "what is", "what've": "what have", "when's": "when is", "when've": "when have", "where'd": "where did", "where's": "where is",

                           "where've": "where have", "who'll": "who will", "who'll've": "who will have", "who's": "who is", "who've": "who have",

                           "why's": "why is", "why've": "why have", "will've": "will have", "won't": "will not", "won't've": "will not have",

                           "would've": "would have", "wouldn't": "would not", "wouldn't've": "would not have", "y'all": "you all",

                           "y'all'd": "you all would","y'all'd've": "you all would have","y'all're": "you all are","y'all've": "you all have",

                           "you'd": "you would", "you'd've": "you would have", "you'll": "you will", "you'll've": "you will have",

                           "you're": "you are", "you've": "you have"}

def contractual_mapping(data):
  s=''
  
  d = data.split(' ')
  for i in range (len(d)):
    try:
      d[i]= contraction_mapping[d[i]]
      #print(f"Worked for {d}. New word is {contraction_mapping[d]}")
    except KeyError:
      #print(f"Didn't work for {d}")
      d[i]=d[i]
      
  return ' '.join(d)

def acceptable_data(data):
    if len(data) <= 1:
        return False
    #elif len(data.split(' ')) < 150:
    #    return False
    
    else:
        return True

def format_data(data):
    w=data
    w = re.sub(r'https?:\/\/.*[\r\n]*', '', w, flags=re.MULTILINE)
    w = re.sub(r'https.*[\r\n]*', '', w, flags=re.MULTILINE)
    w = re.sub(r"[^a-zA-Z?.!,¿ ]+", "", w) #new one for bert
   
    w= contractual_mapping(w)
    #print(w)

    return w

    
def to_sentences(data,keep_array=False):
  #text = "God is Great! I won a lottery."
  #Output: ['God is Great!', 'I won a lottery ']
  d= sent_tokenize(data)
  if not keep_array:
    return '\n'.join(d)
  else:
    return d
  

def summarise(subr,num_posts=1):    
    """
    Returns summary, details where
    summary is a dict of the summary for each post, if user chose more than one post
    details gives details about the post like the poster, date.
    """
    sub = subr
    limit=num_posts
    start_time = time.time()
    articles=[]
    data=''
    acc_data=0
    titles=[]
    datePosts=[]
    error=0
    try:
        for submission in reddit.subreddit(sub).top(limit=1000):
            
            if acc_data==limit:
                break
            if submission.selftext!=' ':
                fsub= format_data(submission.selftext)
                if acceptable_data(fsub):
                    acc_data+=1
                    data=fsub
                    datePosts.append(datetime.datetime.fromtimestamp(submission.created))
                    titles.append(submission.title)             
                    articles.append(to_sentences(data))
    except Exception as e:
        error=1
        return {'error':e}, None
        
    model = Summarizer()

    #Details of the posts to be summarised.
    details={
        'subreddit':subr,
        'title':titles,
        'date':datePosts
       
    }
    summary={}
    for i in range(len(articles)):
      result = model(articles[i],num_sentences=1,max_length=250)
      full = ''.join(result)
      summary.update({i:full})

    return summary,details
    
   
#summary,details = summarise()   
#print(f"Summary for post: \n {summary} \n Details: {details}")