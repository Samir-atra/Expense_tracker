"""generates an interface for the user to input data"""

import sys
import PySimpleGUI as sg


def gui_function(win_title, text1, text2, submit, cancel, size):
    """
    generating the graphical user interface for the user to input data
    providing two sizes of the window first for layout with two inputs
    and the second for layout with one input

    Args:
        win_title: the title of the window
        text1: the text of the first input
        text2: the text of the second input
        submit: the text of the submit button
        cancel: the text of the cancel button
        size: the size of the layout

    Returns:
        event: the event of the button clicked
        values: the values of the outputs
    """

    layout = []

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
