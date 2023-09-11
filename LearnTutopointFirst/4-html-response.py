from fastapi.responses import HTMLResponse
from fastapi import FastAPI
app = FastAPI()
@app.get("/hello/")
async def hello():
   ret='''
<html>
<body>
<h2>Hello World!</h2>
</body>
</html>
'''
   return HTMLResponse(content=ret)