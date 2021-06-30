import PySimpleGUI as psg

layout = [
    [psg.Text("Hi, my name is MARTIN DELUX", font=("Arial", 30))],
    [psg.Button("Ok", font=("Arial", 32, "normal"))]
]

window = psg.Window(title="Program", layout=layout, margins=(400, 400))

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        break

    if event == "Hatfu!!!":
        break

window.close()
