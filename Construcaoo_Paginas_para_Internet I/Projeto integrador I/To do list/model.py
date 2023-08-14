from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

tasks=[]

class Task(BaseModel):
    id:int
    name:str
    status:str='incomplete'