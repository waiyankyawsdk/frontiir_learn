import uvicorn
from fastapi import FastAPI, Body
from typing import List
from pydantic import BaseModel, Field

app = FastAPI()
class Student(BaseModel):
    id : int
    name : str = Field(None, title="name of student", max_length=15)
    subjects : List[str] = []

@app.post("/students")
async def student_data(name : str = Body(...), marks : int = Body(...)):
    return {"name" : name, "marks" : marks}

@app.post('/students/{college}')
async def student_data(college : str, age:int , student : Student):
    return {"college" : college, "age" : age, **student.dict()}
