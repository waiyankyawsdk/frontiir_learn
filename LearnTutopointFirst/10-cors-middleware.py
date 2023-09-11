from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
   "http://192.168.211.1:8000",
   "http://localhost",
   "http://localhost:8080",
   "http://127.0.0.1:5500",

]
app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)
@app.get("/")
async def main():
   return {"message": "Hello World"}