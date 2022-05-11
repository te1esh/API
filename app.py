from fastapi import FastAPI

app = FastAPI()  # create object app from class fastAPI


@app.get("/")
def hello_world():
    return "hello, world"
