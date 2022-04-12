from ctypes.wintypes import SIZE
from tkinter import CENTER, Scale
import PySimpleGUI as app


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
        print(TokenValue)

    if button == 'UNINSURED':
        TokenValue = 2
        print(TokenValue)

# Close program.
window.close()
