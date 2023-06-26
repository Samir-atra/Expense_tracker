import PySimpleGUI as sg
import sys


def gui_function(win_title, text1, text2, submit, cancel, size):
    # a function for generating the graphical user interface for the project
    if size == 1:
        layout = [
            [sg.Text(text1)],
            [sg.InputText()],
            [sg.Submit(submit), sg.Cancel(cancel)],
        ]
    elif size == 2:
        layout = [
            [sg.Text(text1)],
            [sg.InputText()],
            [sg.Text(text2)],
            [sg.InputText()],
            [sg.Submit(submit), sg.Cancel(cancel)],
        ]

    window = sg.Window(win_title, layout)

    event, values = window.read()
    if event == "Cancel":
        sys.exit()
    window.close()

    return event, values


if __name__ == "__main__":
    gui_function()
