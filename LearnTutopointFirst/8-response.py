from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()

class Student(BaseModel):
    id : int
    name : str = Field(None, title="name of student" , max_length=10)
    marks : List[int] = []
    percent_marks : float

class Percent(BaseModel):
    id : int
    name : str = Field(None, title="name of student", max_length=10)
    percent_marks : float

@app.post("/marks", response_model=Percent)
async def get_percent(stu: Student):
    stu.percent_marks = sum(stu.marks) / len(stu.marks)
    return stu