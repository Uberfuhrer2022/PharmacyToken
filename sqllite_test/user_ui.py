from tokenize import Token
import PySimpleGUI as app
import random
import datetime
import sqlite3

db_file = "database.db"

x = datetime.datetime.now()


def generate_token():
    global total_tokens
    global waiting_time 
    global queue_length 
    global time_needed 
    total_tokens =+ 1
    waiting_time =+ 5
    queue_length =+ 1
    time_needed = waiting_time * queue_length
    
    Token = random.randrange(1,1000)


    with sqlite3.connect(db_file) as conn:
        if conn.execute("SELECT 1 FROM tokens WHERE numbers = (?)", (Token,)).fetchone():
            Token = random.randrange(0,100)
        else:
            print(x.strftime("%d-%b-%y"))
            print(x.strftime("%H:%M:%S"))
            print("Your ticket number is:", Token)
            
            conn.execute("INSERT INTO tokens VALUES (?)", (Token,))

layout = [
    [app.Text('')],
    [app.Text('')],
    # [app.Text('ASTER PHARMACY', font=("Arial", 14))],
    [app.Image('Logo150.png')],
    [app.Text('TOKEN DISPENSARY', font=("Arial", 18, "bold"))],
    [app.Text('')],
    [app.ReadFormButton('INSURED', font=(
        "Courier New", 12, 'bold'), size=(30, 5))],
    [app.ReadFormButton('UNINSURED', font=(
        "Courier New", 12, 'bold'), size=(30, 5))],
]

# Application Window
window = app.Window("Token Dispenser", layout, size=(
    500, 550), element_justification='center')

# Events Loop (infinite to keep program running)

# TokenValue: 0 (UNDECIDED), 1 (INSURED), 2 (UNINSURED)
TokenValue = 0

while True:
    button, values = window.read()

    if button == app.WIN_CLOSED:  # If user presses X on program window.
        break

    if button == 'INSURED':
        TokenValue = 1
        print(TokenValue, Token)

    if button == 'UNINSURED':
        TokenValue = 2
        print(TokenValue, Token)

# Close program.
window.close()