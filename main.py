import random
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/testei")
async def funcaoteste():
    return { "teste": True, "num_aleatorio": random.randit ( 0,  1000)}
