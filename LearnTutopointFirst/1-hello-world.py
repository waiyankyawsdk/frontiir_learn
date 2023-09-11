from fastapi import FastAPI, Path, Query
app = FastAPI()

@app.get("/")
async def index():
    return {"message" : "Hello World"}

@app.get("/hello/{name}/{age}")
async def hello(*, name : str = Path(..., min_length=3, max_length=10), \
    age: int = Path(..., ge=1, le=100), \
    percent : float = Query(..., ge=0, le=100)):
    return {"name" : name, "age" : age}