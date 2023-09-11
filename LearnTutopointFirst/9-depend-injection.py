from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException
app = FastAPI()

# async def dependency(id: str, name : str, age : int):
#     return {"id" : id, "name" : name, "age" : age}
class dependency:
    def __init__(self, id: str, name: str, age: int) -> None:
        self.id = id
        self.name = name
        self.age = age

async def validate(dep: dependency = Depends(dependency)):
    if dep.age > 18:
        raise HTTPException(status_code=400, detail="You are not eligible")

@app.get("/users", dependencies=[Depends(validate)])
async def user(dep : dependency = Depends(dependency)):
    return {**dep.__dict__, "message" : "You are eligible"}

@app.get("/admin")
async def admin(dep : dependency = Depends(dependency)):
    return dep

# async def get_db():
#    db = DBSession()
#       try:
#          yield db
#       finally:
#             db.close()