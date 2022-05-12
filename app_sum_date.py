import datetime

from fastapi import FastAPI

app = FastAPI()  # create object app from class fastAPI


@app.get("/sum_date")
def sum(current_date : datetime.date, offset : int) -> datetime.date:
    return current_date + datetime.timedelta(days=offset)