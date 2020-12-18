from typing import List

from fastapi import FastAPI, File, UploadFile, HTTPException, Depends


app = FastAPI()

@app.get("/test")
def predict():
    print('Test')
