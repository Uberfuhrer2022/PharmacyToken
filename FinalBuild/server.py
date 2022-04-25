import PySimpleGUI as app
import random

from datetime import datetime
from fastapi import FastAPI, Path


my_app = FastAPI()
app.counter = 129

@my_app.get("/")
def root():
    return {"Message": "This is a Token dispenser machine"}


# Date and Time
CurrentDay = datetime.today()
CurrentTime = datetime.now()
tokDate = CurrentDay.strftime("%d-%b-%Y")
tokTime = CurrentTime.strftime("%H:%M:%S")
Token = "UNASSIGNED"


################ Generate Token/Date/Time for JSON DB ################

@my_app.get("/get_token")
def CreateToken():
    global total_tokens
    global waiting_time
    global queue_length
    global time_needed
    total_tokens = +1
    waiting_time = +5
    queue_length = +1
    time_needed = waiting_time * queue_length
    GeneratedID = str(random.randint(123456789, 987654321))

    global Token
    global TokenNum
    Token = str("-".join(GeneratedID[i : i + 3] for i in range(0, len(GeneratedID), 3)))
    app.counter += 4
    TokenNum = app.counter
    waiting_time = waiting_time+5
    finalToken = {
        "Token ID:": Token,
        "Token Number": TokenNum,
        "Date:": tokDate,
        "Time:": tokTime,
        "Waiting Time:": waiting_time,
    }
    return finalToken


@my_app.get("/report")
def report_stats():
    finalStats = {
        "Total tokens:": total_tokens,
        "Waiting time:": waiting_time,
        "Queue length:": queue_length,
        "Time needed:": time_needed,
    }
    return finalStats

