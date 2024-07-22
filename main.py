import os
import io
import time
import numpy as np
import pandas as pd
from PIL import Image
from typing import Optional, Annotated, Union


from fastapi import FastAPI, File, UploadFile, HTTPException, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import requests

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class XValues(BaseModel):
    x1: int

class ExchangeFormat(BaseModel):
    x: XValues = None
    api_key: Union[str, None] = None
    api_secret: Union[str, None] = None
    #description: str | None = None
    #price: float
    #tax: float | None = None

@app.get("/")
def read_root():
    return RedirectResponse("/static/index.html")

def valid_secret(api_key, api_secret):
    # usually here would be sql query to check if api_key and api_secret are valid
    if api_key == "d2ad67989fc0dfb80672be820e8f0ca263a07541ab805b05e46de8a759879eac" or api_secret == "09c8ee34fd943c30ce6a00a55f8ebbf22bf9f3864b4d2e70120afc23837f7d4d":
        return True
    return False


def predict_query(payload):
    API_URL = "https://hjropwsuc4psaxqo.eu-west-1.aws.endpoints.huggingface.cloud"
    headers = {
        "Accept" : "application/json",
        "Content-Type": "application/json" 
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

@app.post("/img")
async def create_upload_file(api_key: Annotated[str, Form()], api_secret: Annotated[str, Form()], upload_file: Annotated[UploadFile, Form()]):
    print(api_key, api_secret)
    if api_key is None and api_secret is None:
        raise HTTPException(status_code=404, detail="missing api_key ore api_secret")
    elif not valid_secret(api_key, api_secret):
        raise HTTPException(status_code=404, detail="invalid api_key ore api_secret")
    
    upload_file_content = await upload_file.read()
    img = Image.open(io.BytesIO(upload_file_content))

    return {}


@app.post("/predict/")
async def predict(values: ExchangeFormat):# -> XVars: 
    
    print(values.api_key, values.api_secret, values.x)
    if values.api_key is None and values.api_secret is None:
        raise HTTPException(status_code=404, detail="missing api_key ore api_secret")
    elif not valid_secret(values.api_key, values.api_secret):
        raise HTTPException(status_code=404, detail="invalid api_key ore api_secret")

    output = predict_query({
        "inputs": [[values.x.x1]],
        "parameters": {}
    })
    return {"result": output[0][0]}
