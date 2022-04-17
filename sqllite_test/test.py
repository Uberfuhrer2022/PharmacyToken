
import random
import datetime
import sqlite3

db_file = "database.db"

x = datetime.datetime.now()


def generate_token():

    global waiting_time 
    global queue_length 
    global time_needed 
    waiting_time =+ 5
    queue_length =+ 1
    time_needed = waiting_time * queue_length
    
    Token = random.randrange(1,1000)
    Counter = random.randrange(1, 10)

    with sqlite3.connect(db_file) as conn:
        if conn.execute("SELECT 1 FROM tokens WHERE numbers = (?)", (Token,)).fetchone():
            Token = random.randrange(0,100)
        else:
            print(x.strftime("%d-%b-%y"))
            print(x.strftime("%H:%M:%S"))
            print("Your ticket number is:", Token)

            print("Please proceed to the counter number:", Counter)
            
            conn.execute("INSERT INTO tokens VALUES (?)", (Token,))

def report_stats():
    print("Average waiting time is:", waiting_time, "minutes")
    print("There are:", queue_length, "people in the queue")
    print("Time needed to clean up the queue is:", time_needed, "minutes")



    

generate_token()
report_stats()