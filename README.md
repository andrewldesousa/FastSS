# reddit4nlp

In this Alexa Skill project, we design two models to perform the following tasks using Reddit data:
1. Syn
2. AlexaSummarise

The models are wrapped around an API on AWS and was deployed using FastAPI.

## Syn
This model will get the synonyms for any word (in English) the user gives. 

As an example, the user can say “Alexa, give me a synonym for _eat_”.

An Alexa replies: 

*Model Used:* The Word2Vec Skipgram model. Word2vec is a technique for learning word embeddings in natural language processing. It uses a neural network model to learn word associations from a large corpus of text. As the name implies, word2vec represents each distinct word with a vector such that we can learn the level of semantic similarity between the words represented by those vectors. 

## AlexaSummarise
Sometimes, it can be tedious to read very long Reddit posts. We may want just a summary of the whole post.

AlexaSummarise is a project that summarizes posts from any subreddit for you. 

As an example, the user says: “Alexa, summarize the latest _1_ post(s) in _learningpython_”

You can specify the subreddit you want and how many posts you want summarized (the default is 1). If the number of posts to be summarized is more than one, Alexa will take turns summarizing each one and giving you the summary (this will definitely take some time).

*NLP Category: Text Summarization*. To achieve this, we used learned BERT sentence embeddings to build an extractive summarizer.

# Project done by 
* Chris Emezue (chris.emezue@tum.de | chris.emezue@gmail.com)
* Andrew Desousa ()

Project was done as part of the Deep learning in NLP Seminar Project of TUM.

# Deployment
sudo scp -i "fast-synonym.pem" output_file.zip ubuntu@ec2-100-26-49-136.compute-1.amazonaws.com:~/reddit4nlp/www/api
