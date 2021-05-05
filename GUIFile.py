import PySimpleGUI as sg

layout = [  [sg.Text("This is a test")]
            [sg.Input()],
            [sg.Button('Submit')]]

window = sg.Window('Testing', layout)

window.close()