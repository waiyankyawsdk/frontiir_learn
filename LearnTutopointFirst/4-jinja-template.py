from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

class User(BaseModel):
   username : str
   password : str

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/hello/{name}", response_class=HTMLResponse)
async def hello(request: Request, name: str):
   return templates.TemplateResponse("hello.html", {"request": request, "name" : name})

@app.get("/login/", response_class=HTMLResponse)
async def login(request: Request):
   return templates.TemplateResponse("login.html", {"request" : request})

@app.post("/submit/", response_model=User)
async def submit(name : str = Form(...), password : str = Form(...)):
   data = {"username": name, "password" : password}
   return User(**data)