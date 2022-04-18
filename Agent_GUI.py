from ctypes.wintypes import SIZE
from tkinter import CENTER, Scale
import PySimpleGUI as app

# PSG Color Theme
app.theme("DefaultNoMoreNagging")

# Layout of Elements

img1 = app.Image('Logo50.png')
img2 = app.Image('Logo80.png')

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
    [app.Text('CUSTOMER QUEUE', font=('Arial', 10, 'bold'))],
    [app.Multiline('#1 - TOKEN: 143', size=(60, 20))]
]

layout = [
    [app.Frame(layout=col_HEADER, title=''), img2],
    [app.Text('')],
    [app.Frame(layout=col_SERVICE, title=''),
     app.Frame(layout=col_COUNTER, title='')]
]

# Application Window
window = app.Window("ASTER PHARMACY - Employee Control Board", layout, size=(
    500, 550))  # ,element_justification='center'


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
            break
        else:
            print('ERROR: Please start your shift before serving customers.')

    if button == 'END SERVICE':
        while DutyAbility == True:
            AgentValue = 400
            print(AgentValue)
            break
        else:
            print('ERROR: Please start your shift before serving customers.')

# Close program.
window.close()
