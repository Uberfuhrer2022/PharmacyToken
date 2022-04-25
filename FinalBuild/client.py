from server import CreateToken
from typing_extensions import Self
from fastapi import FastAPI
from cgi import test
from ctypes.wintypes import SIZE
from tkinter import CENTER, Scale
import PySimpleGUI as app
import requests

# PSG Color Theme
app.theme("DefaultNoMoreNagging")

# Layout of Elements
layout = [
    [app.Text('')],
    [app.Text('')],
    # [app.Text('ASTER PHARMACY', font=("Arial", 14))],
    [app.Image('Logo150.png')],
    [app.Text('TOKEN DISPENSARY', font=("Arial", 18, "bold"))],
    [app.Text('')],
    [app.ReadFormButton('PRINT TOKEN', font=(
        "Courier New", 14, 'bold'), size=(30, 6), key=('-PRINTER-'))]
]

# Application Window
window = app.Window("Token Dispenser", layout, size=(
    500, 470), element_justification='center')

# Events Loop (infinite to keep program running)

# TokenValue: 0 (UNDECIDED), 1 (INSURED), 2 (UNINSURED)
TokenValue = 0

client_app = FastAPI()


# from server import CreateToken


while True:
    button, values = window.read()

    if button == app.WIN_CLOSED:  # If user presses X on program window.
        break

    if button == 'PRINT TOKEN':
        TokenValue = 1
        print(TokenValue)
        # GUI IS NOT FUNCTIONAL

# Close program.
window.close()
