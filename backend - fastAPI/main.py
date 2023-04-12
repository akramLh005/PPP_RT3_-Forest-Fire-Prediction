from fastapi import FastAPI 
from pydantic import BaseModel
app=FastAPI()

class person (BaseModel):
    first_name : str 
    last_name :  str
    
    

@app.get("/")
def main_Page():

    return {"msg":"hellooooo"}

#@app.post(/api/v1/add)
#async def add_person():
