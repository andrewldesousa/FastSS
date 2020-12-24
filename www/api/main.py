import numpy as np
import pandas as pd
import os
import tempfile

from typing import List

from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from pydantic import BaseModel, ValidationError, validator
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY


app = FastAPI()


@app.get("/synonyms")
def predict(word: str):
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
    f.close()
    os.remove(file_name)

    return {'synonyms': output}