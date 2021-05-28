import PySimpleGUI as psg
import os


column1 = [
    [
        psg.Text("Gallery", font=("Arial", 20)),
        psg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        psg.FolderBrowse(),

    ],
    [
        psg.Listbox(
            values=[],
            enable_events=True,
            size=(40, 10),
            key="-FILE LIST-"
        )
    ],

]


column2 = [
    [psg.Text("Choose an image:")],
    [psg.Text(size=(40, 1), key="-TOUT-")],
    [psg.Image(key="-IMAGE-")],
]


layout = [[
    psg.Column(column1),
    psg.VSeparator(),
    psg.Column(column2)
]]

window = psg.Window("Gallery", layout)

while True:
    event, values = window.read()

    if event == psg.WIN_CLOSED:
        break

    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [f for f in file_list if os.path.isfile(
            os.path.join(folder, f)) and f.lower().endswith(".png")]

        window["-FILE LIST-"].update(fnames)

    if event == "-FILE LIST-":
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0])
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass


window.close()
