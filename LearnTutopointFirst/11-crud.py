from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from id_generator import sequence_id

app = FastAPI()
data = []

class Book(BaseModel):
    id : int
    title : str
    author : str
    publisher : str

@app.post("/book")
def add_book(book : Book):
    if book.id is 0:
        book.id = next(sequence_id)
    data.append(book.dict())
    return data

@app.get("/book")
def get_books():
    return data

@app.get("/book/{id}")
def get_book(id : int):
    return data[id -1]

@app.put("/book/{id}")
def update_book(id : int, book : Book):
    data[id -1] = book
    return data

@app.delete("/book/{id}")
def remove_book(id : int):
    return data.pop(id-1)
