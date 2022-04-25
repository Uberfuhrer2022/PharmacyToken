import PySimpleGUI as app
import random
from datetime import datetime
from fastapi import FastAPI, Path

my_app = FastAPI()

# COUNTERS (for increments)
app.tokNumber = 100
app.totalToks = 0
app.waitTime = 0
app.queLength = 0
app.rep_tokNumber = 101


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

    app.totalToks += 1
    total_tokens = app.totalToks

    app.waitTime += 5
    waiting_time = app.waitTime

    app.queLength += 1
    queue_length = app.queLength

    time_needed = waiting_time * queue_length
    GeneratedID = str(random.randint(123456789, 987654321))

    global Token
    global TokenNum
    Token = str("-".join(GeneratedID[i: i + 3]
                for i in range(0, len(GeneratedID), 3)))
    app.tokNumber += 1
    TokenNum = app.tokNumber

    finalToken = {
        "Token ID": Token,
        "Token Number": TokenNum,
        "Date": tokDate,
        "Time": tokTime,
        "Waiting Time": waiting_time,
    }

    queueDetails = {
        "Number of Customers in Queue": queue_length
    }
    return finalToken, queueDetails

# RUN IN TERMINAL TO ACTIVIATE SERVER
# uvicorn --host 0.0.0.0 --port 8000 server:my_app --reload


@my_app.get("/report")
def report_stats():
    app.rep_tokNumber

    global TokenNumber
    app.rep_tokNumber += 1
    TokenNumber = app.rep_tokNumber

    finalStats = {
        "Total tokens": total_tokens,
        "Waiting time": waiting_time,
        "Queue length": queue_length,
        "Time needed": time_needed,
        "Token Number": TokenNumber
    }
    return finalStats
