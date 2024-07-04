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
    pass

class ExchangeFormat(BaseModel):
    pass

@app.get("/")
def read_root():
    return RedirectResponse("/static/index.html")

def valid_secret(api_key, api_secret):
    # usually here would be sql query to check if api_key and api_secret are valid
    if api_key == "d2ad67989fc0dfb80672be820e8f0ca263a07541ab805b05e46de8a759879eac" or api_secret == "09c8ee34fd943c30ce6a00a55f8ebbf22bf9f3864b4d2e70120afc23837f7d4d":
        return True
    return False


def predict_query(payload):
    API_URL = "YOUR QUERY URL"
    headers = {
        "Accept" : "application/json",
        "Content-Type": "application/json" 
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

@app.post("/img")
async def create_upload_file():
    pass


@app.post("/predict/")
async def predict(values: ExchangeFormat):
    pass
