# FastS<sup>2</sup>:zap:

In this Alexa Skill project, we design two models using Reddit data:
1. FastSynonym
2. FastSummarise

The models are wrapped around an API on AWS and was deployed using [FastAPI](https://fastapi.tiangolo.com/).

## FastSynonym
This model will get the synonyms for any word (in English) the user gives. As an example, the user can say 
<p align="center">
“Alexa, what's another word for <ins>eat</ins> ?”.
</p>

**Model Used: The Word2Vec Skipgram model.**

Word2vec is a technique for learning word embeddings in natural language processing. It uses a neural network model to learn word associations from a large corpus of text. As the name implies, word2vec represents each distinct word with a vector such that we can learn the level of semantic similarity between the words represented by those vectors. 

## FastSummarise
It is very important to be informed of the latest things happening around our world in different areas of life (medicine, agriculture, science, etc). This is why Reddit is a suitable platform to get latest posts on. However, it can be tedious to read very long Reddit posts. We may want just a summary of the whole post.

FastSummarise is a project that summarises the latest posts from any subreddit for you. As an example, the user says:
<p align="center">
  “Alexa, summarize the latest <ins>1</ins> post(s) in <ins>learningpython</ins>”
  </p>

The user can specify the subreddit you want and how many posts you want summarized (the default is 1). If the number of posts to be summarized is more than one, Alexa will take turns summarizing each one and giving you the summary (this will definitely take some time).

**NLP Category: Text Summarization**

To achieve this, we used learned BERT sentence embeddings to build an extractive summarizer. In extractive text summarization, we aim to use deep learning to identify the important sentences or excerpts from a large text. Our extractive summarizer uses the HuggingFace Pytorch transformers library to run extractive summarizations. It does this by first embedding the sentences, then running a clustering algorithm, finding the sentences that are closest to the cluster's centroids. 

# Project Contributors 
* Chris Emezue (chris.emezue@tum.de | chris.emezue@gmail.com)
* Andrew Desousa ()

Project was executed as part of the Deep learning in NLP Seminar Project of TUM.

