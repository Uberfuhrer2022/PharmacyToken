from ctypes.wintypes import SIZE
from tkinter import CENTER, Scale
import PySimpleGUI as app
import random
import json
from datetime import datetime

# Date and Time
CurrentDay = datetime.today()
CurrentTime = datetime.now()
tokDate = CurrentDay.strftime("%d-%b-%Y")
tokTime = CurrentTime.strftime("%H:%M:%S")
Token = 'UNASSIGNED'

# PSG Color Theme
app.theme("DefaultNoMoreNagging")


################ Generate Token/Date/Time for JSON DB ################

def CreateToken():
    GeneratedID = str(random.randint(123456789, 987654321))

    global Token
    Token = str('-'.join(GeneratedID[i:i+3]
                         for i in range(0, len(GeneratedID), 3)))
    print(f'Generated Token: {Token}')
    print(f'Date and Time: {tokDate}, {tokTime}')


######################################################################


# Layout of Elements
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


def Insurance_False():
    with open("TokenFile.json") as json_file:
        data = json.load(json_file)
        temp = data["Tokens"]
        entryDATA = {"TokenID": Token, "Date": tokDate,
                     "Time": tokTime, "Insurance": False}
        temp.append(entryDATA)
    write_json(data)


def Insurance_True():
    with open("TokenFile.json") as json_file:
        data = json.load(json_file)
        temp = data["Tokens"]
        entryDATA = {"TokenID": Token, "Date": tokDate,
                     "Time": tokTime, "Insurance": True}
        temp.append(entryDATA)
    write_json(data)


while True:
    button, values = window.read()

    if button == app.WIN_CLOSED:  # If user presses X on program window.
        break
    if button == 'INSURED':
        CreateToken()

        def write_json(data, filename='TokenFile.json'):
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
        Insurance_True()

    if button == 'UNINSURED':
        CreateToken()

        def write_json(data, filename='TokenFile.json'):
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
        Insurance_False()


# Close program.
window.close()
