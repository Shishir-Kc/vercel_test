from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import os 

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Anyone can access
    allow_methods=["*"],
    allow_headers=["*"],
)

app.get("/hi/")
def read_root():
    return {"Hello": "World"}


