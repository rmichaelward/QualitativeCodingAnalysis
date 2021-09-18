#main file
#imports modules and starts GUI

import PySimpleGUI as sg

if __name__ == '__main__' :
    layout = [[sg.Text("Main Menu")], [sg.Button("END")], [sg.Button("MODELS")]]

    # Create the window
    window = sg.Window("Qualitative Analysis", layout)
    
    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "END" or event == sg.WIN_CLOSED:
            break

window.close()
