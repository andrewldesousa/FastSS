# FastS<sup>2</sup>:zap:

In this Alexa Skill project, we design two models using Reddit data:
1. FastSynonym
2. FastSummarize

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

FastSummarize is a project that summarises the latest posts from any subreddit for you. As an example, the user says:
<p align="center">
  “Alexa, summarize the latest post in <ins>learningpython</ins>”
  </p>

The user can specify the subreddit you want and how many posts you want summarized (the default is 1). If the number of posts to be summarized is more than one, Alexa will take turns summarizing each one and giving you the summary (this will definitely take some time).

**NLP Category: Text Summarization**

To achieve this, we used learned BERT sentence embeddings to build an extractive summarizer. In extractive text summarization, we aim to use deep learning to identify the important sentences or excerpts from a large text body. Our extractive summarizer uses the HuggingFace Pytorch transformers library to run extractive summarization. It does this by first encoding the sentences into embedding representations, running a clustering algorithm, then finding the sentences that are closest to the cluster's centroids.

**Some Photos**

![Example1](https://user-images.githubusercontent.com/36100251/106934345-12b46900-672b-11eb-9e49-a650976bf20e.jpeg)
![Example2](https://user-images.githubusercontent.com/36100251/106934355-15af5980-672b-11eb-9c6b-33486cc2bb5d.jpeg)

# Project Contributors 
* Chris Emezue (chris.emezue@tum.de | chris.emezue@gmail.com)
* Andrew Desousa

Project was executed as part of the Deep learning in NLP Seminar Project of TUM.

