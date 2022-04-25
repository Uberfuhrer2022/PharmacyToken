from server import tokDate, tokTime
import json
import requests
from ctypes.wintypes import SIZE
from lib2to3.pgen2.token import NEWLINE
from tkinter import CENTER, Scale
import PySimpleGUI as app
from fastapi import FastAPI


# PSG Color Theme
app.theme("DefaultNoMoreNagging")

# Layout of Elements

img1 = app.Image('Logo50.png')

col_HEADER = [
    [app.Text('ASTER PHARMACY - CITY WALK BRANCH', font=('Arial', 8, 'bold'))],
    [app.Text('EMPLOYEE CONTROL BOARD', font=('Aria;', 18, 'bold'))]
]

col_SERVICE = [
    [app.Text('SERVICE PANEL')],
    [app.ReadFormButton('START SHIFT', font=(
        "Courier New", 12, 'bold'), size=(20, 5))],
    [app.ReadFormButton('REQUEST CUSTOMER', font=(
        "Courier New", 12, 'bold'), size=(20, 5))],
    [app.ReadFormButton('END SERVICE', font=(
        "Courier New", 12, 'bold'), size=(20, 5))],
]


col_COUNTER = [
    [app.Text('CUSTOMER DETAILS', font=('Arial', 10, 'bold'))],
    [app.Multiline('Request a new customer to start.', size=(
        60, 10), key=('-QUEUE-'), font=('Courier New', 12))],
    [app.Text('QUEUE COUNTER PANEL', font=('Arial', 10, 'bold'))],
    [app.Multiline(f'|-------------------------- {tokDate} --|-- {tokTime} ----|', size=(
        60, 6), key=('-Q_COUNTER-'), font=('Tahoma', 12))]
]

layout = [
    [app.Frame(layout=col_HEADER, title=''), img1],
    [app.Text('')],
    [app.Frame(layout=col_SERVICE, title=''),
     app.Frame(layout=col_COUNTER, title='')]
]

# Application Window
window = app.Window("ASTER PHARMACY - Employee Control Board", layout, size=(
    700, 550))  # ,element_justification='center'


# AgentValue: 200 (REQUESTING CUSTOMER), 400 (ENDING SERVICE)
# DutyAbility: allows Agent to use request customer/end service buttons.

AgentValue = 0
DutyAbility = False


while True:
    button, values = window.read()

    if button == app.WIN_CLOSED:  # If user presses X on program window.
        break

    if button == 'START SHIFT':
        DutyAbility = True
        print(DutyAbility)

    if button == 'REQUEST CUSTOMER':
        while DutyAbility == True:
            AgentValue = 200
            print(AgentValue)

            api_url = 'http://localhost:8000/get_token'
            response = requests.get(api_url)
            print(response)

            data = response.text
            parse_json = json.loads(data)
            print(parse_json)

            text = window['-QUEUE-']
            window.FindElement('-QUEUE-').Update('')

            # FULL DATA LENGTH
            # text.update(text.get()+f"\n{str(parse_json)}")
            remove_chars = "('),"

            # Token Number
            token_number = parse_json[0]
            tokNumRow = ('Token Number: ',
                         token_number['Token Number'])  # Token Number
            new_tokNum = str(tokNumRow)

            for chars in remove_chars:
                new_tokNum = new_tokNum.replace(chars, '')
            text.update(text.get()+f"\n{str(new_tokNum)}")

            # Token ID
            token_ID = parse_json[0]
            tokIDRow = ('Token ID: ',
                        token_ID['Token ID'])  # Token ID
            new_tokID = str(tokIDRow)

            for chars in remove_chars:
                new_tokID = new_tokID.replace(chars, '')
            text.update(text.get()+f"\n{str(new_tokID)}")

            # Customer Queue Length
            queue_number = parse_json[1]
            queNumRow = ('Number of Customers in Queue: ',
                         queue_number['Number of Customers in Queue'])
            new_queNum = str(queNumRow)

            for chars in remove_chars:
                new_queNum = new_queNum.replace(chars, '')
            text.update(text.get()+f"\n\n\n\n{str(new_queNum)}")

            # ------| CUSTOMER COUNTER BELOW! | ------ #
            api_url = 'http://localhost:8000/report'
            response = requests.get(api_url)
            print(response)

            data = response.text
            parse_json = json.loads(data)
            print(parse_json)

            text2 = window['-Q_COUNTER-']
            # window.FindElement('-Q_COUNTER-').Update('') <-- clears text before appending

            # FULL DATA LENGTH
            # text.update(text.get()+f"\n{str(parse_json)}")
            remove_chars = "('),"

            # Token Number
            last_token = parse_json
            q_Number = ('Token Number: ',
                        last_token['Token Number'])  # Last Token
            newq_Number = str(q_Number)

            for chars in remove_chars:
                newq_Number = newq_Number.replace(chars, '')
            text2.update(text2.get()+f"\n{str(newq_Number)}")

            break
        else:
            print('ERROR: Please start your shift before serving customers.')

    if button == 'END SERVICE':
        while DutyAbility == True:
            AgentValue = 400
            print(AgentValue)
            window.close()
            break
        else:
            print('ERROR: Please start your shift before serving customers.')

# Close program.
window.close()
