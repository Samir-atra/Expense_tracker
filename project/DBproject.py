"""
create functions for:
    - creating the database if not exists
    - creating a table with the month date if not exists
    - make an entry to the table 
    - table updater for new budget
    - generating a pdf report
    - build a gui for the project.
    - check the queries quality and safty
"""

from flask import Flask, g
import sqlite3
from datetime import datetime
import os
import time as tm
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import argparse
import re
import sys
import textwrap
import PySimpleGUI as sg
from .

# def gui_function(win_title, text1, text2, submit, cancel, size):
#     # a function for generating the graphical user interface for the project
#     if size == 1:
#         layout = [
#             [sg.Text(text1)],
#             [sg.InputText()],
#             [sg.Submit(submit), sg.Cancel(cancel)],
#         ]
#     elif size == 2:
#         layout = [
#             [sg.Text(text1)],
#             [sg.InputText()],
#             [sg.Text(text2)],
#             [sg.InputText()],
#             [sg.Submit(submit), sg.Cancel(cancel)],
#         ]

#     window = sg.Window(win_title, layout)

#     event, values = window.read()
#     if event == "Cancel":
#         sys.exit()
#     window.close()

#     return event, values

########################################################################################################

Database = "/home/samer/Desktop/Beedoo/Expenses_tracker/project/budgeting.db"

db = sqlite3.connect(Database)

month = datetime.now().strftime("%B_%Y")

cursor = db.cursor()

create_table_query = f"CREATE TABLE IF NOT EXISTS {month} (Id INTEGER PRIMARY KEY AUTOINCREMENT, Budget INTEGER, Withdraw INTEGER, Amount_left INTEGER, Withdrawal_purpose TEXT, Date TEXT, Time TEXT)"


create_table = cursor.execute(create_table_query)


db.commit()

###############################################################################################

# date = datetime.now().strftime("%x")
# time = datetime.now().strftime("%X")


# _, budget_sources = gui_function(
#     "Budget",
#     "The amount of money for the month: ",
#     "Sources of the budget: ",
#     "Submit",
#     "Cancel",
#     2,
# )


# budget = int(budget_sources[0])

# sources = budget_sources[1]

# init_entry_query = f"INSERT INTO {month} (Budget, Withdraw, Amount_left, Withdrawal_purpose, Date, Time) VALUES (?, 0, ?, ?, ?, ?);"

# init_entry_args = (budget, budget, f"First entry budget source(s): {sources}", date, time)

# init_entry = cursor.execute(init_entry_query, init_entry_args)

# db.commit()
# ##########################################################################################

# _, withdraw_amount_purpose = gui_function(
#                 "Withdrawal",
#                 "The amount to be withdrawn: ",
#                 "The purpose of this withdrawal: ",
#                 "Submit",
#                 "Cancel",
#                 2,
#             )

# withdraw = withdraw_amount_purpose[0]

# withdrawal_purpose = withdraw_amount_purpose[1]

# make_an_entry_query = f"INSERT INTO {month} (Budget, Withdraw, Amount_left, Withdrawal_purpose, Date, Time) VALUES (?, ?, ?, ?, ?, ?)"

# cursor.execute(f"SELECT * FROM {month}")

# fetch =  cursor.fetchall()

# fetch = fetch[-1][2]

# left = int(fetch) - int(withdraw)

# make_an_entry_args = (fetch, withdraw, left, withdrawal_purpose, date, time)

# make_an_entry = cursor.execute(make_an_entry_query, make_an_entry_args)


# db.commit()

#####################################################################################################

_, budget_sources = gui_function(
    "Budget_update",
    "New budget sources (usage: source1+source2+source3+...): ",
    "Added budget amount: ",
    "Submit",
    "Cancel",
    2,
)

new_sources = budget_sources[0]

added_budget = budget_sources[1]

added_budget = int(budget_sources[1])

count_query = f"SELECT COUNT(*) FROM {month};"

cursor.execute(count_query)

fetch =  cursor.fetchall()

count_fetch = fetch[0][0]

for row in range(count_fetch):
    cursor.execute(f"SELECT * FROM {month}")

    fetch =  cursor.fetchall()

    old_budget = fetch[-1][1]
    old_left = fetch[-1][3]
    old_purpose = str(fetch[0][4])

    new_budget = added_budget + old_budget
    new_left = added_budget + old_left
    new_purpose = old_purpose + new_sources

    update_query = f"UPDATE {month} SET Withdrawal_purpose = ?, Budget = ?, Amount_left = ? WHERE id = {row+1};"

    update_args = (new_purpose, new_budget, new_left)

    cursor.execute(update_query, update_args)

    db.commit()

