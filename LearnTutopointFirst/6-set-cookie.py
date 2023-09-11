from fastapi import FastAPI, Cookie, Response
from fastapi.responses import JSONResponse

app = FastAPI()
@app.post("/cookie/")
def create_cookie():
    content = {"message" : "cookie set"}
    response = JSONResponse(content=content)
    response.set_cookie(key="username", value="admin")
    return response

@app.get("/readcookie")
async def read_cookie(username : str = Cookie(None)):
    return {"username" : username}

@app.delete("/cookie/")
def delete_cookie(response: Response):
    content = {"message": "cookie deleted"}
    response = JSONResponse(content=content)
    response.delete_cookie(key="username")
    return response
