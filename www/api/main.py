import numpy as np
import pandas as pd
import os
import tempfile

from typing import List

from fastapi import FastAPI, File, UploadFile, HTTPException, Depends, BackgroundTasks
from pydantic import BaseModel, ValidationError, validator
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from .alexasummarise import summarise

app = FastAPI()

synonyms_results_dict = {}
summary_result_output = None

def run_synonym_model(word: str):
    file_name = 'temp_file.txt'
    results = str(os.system(f'echo "{word}" | /fastText/fasttext nn /result/fil9.bin >> {file_name}'))
    f = open('temp_file.txt', 'r')
    lines = f.readlines()
    i = 0
    output = []
    for line in lines:
        line = line.split(' ')
        if i == 0:
            line = line[2:]
        elif i == len(lines)-1:
            break
        else:
            pass
        i += 1
        output.append(line[0])
    os.remove(file_name)
    global synonyms_results_dict
    synonyms_results_dict[word] = output

def run_summary_model(subreddit, num_posts=1):
    global summary_result_output
    summary, details = summarise(subreddit, num_posts)
    summary_result_output = summary

@app.get("/synonyms")
def synonyms(word: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(run_synonym_model, word)
    return {'synonyms': 'running task...'}


@app.get("/synonyms_results")
def synonyms_results(word: str):
    global synonyms_results_dict
    output = {word: synonyms_results_dict[word]}
    
    if synonyms_results_dict[word]:
        del synonyms_results_dict[word]
    return output


@app.get("/summary_results")
def summary_results():
    global summary_result_output
    return {'summaries': summary_result_output}

@app.get("/summarize")
def summarize(subreddit: str, num_posts: int, background_tasks: BackgroundTasks):
    global summary_result_output
    summary_result_output = None
    background_tasks.add_task(run_summary_model, subreddit, num_posts=num_posts)
    return {'summaries': 'Running model'}


