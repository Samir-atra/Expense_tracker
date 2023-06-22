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
import argparse
import re
import sys
import csv
from utils.report_generator import generate_report    # this import must be commented for the tests to run.



Database = "budgeting.db"

db = sqlite3.connect(Database)

month = datetime.now().strftime("%B_%Y")

date = datetime.now().strftime("%x")
time = datetime.now().strftime("%X")

cursor = db.cursor()



def db_check_existence(tablename):

    check_exictance_query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tablename}';"

    check_query = cursor.execute(check_exictance_query)

    db.commit()

    fetch = cursor.fetchall()

    if fetch == []:
        return True
    else:
        return False



def db_first_entry(tablename, budget, sources, currency):

    create_table_query = f"CREATE TABLE IF NOT EXISTS {tablename} (Id INTEGER PRIMARY KEY AUTOINCREMENT, Budget INTEGER, Withdraw INTEGER, Amount_left INTEGER, Withdrawal_purpose TEXT, Date TEXT, Time TEXT)"

    create_table = cursor.execute(create_table_query)

    db.commit()

    budget = int(budget)

    sources = sources

    init_entry_query = f"INSERT INTO {tablename} (Budget, Withdraw, Amount_left, Withdrawal_purpose, Date, Time) VALUES (?, 0, ?, ?, ?, ?);"

    init_entry_args = (budget, budget, f"First entry budget source(s): {sources}, currency of the file: {currency}", date, time)

    init_entry = cursor.execute(init_entry_query, init_entry_args)

    db.commit()
    return budget


def db_make_an_entry(tablename, withdraw, purpose):


    make_an_entry_query = f"INSERT INTO {tablename} (Budget, Withdraw, Amount_left, Withdrawal_purpose, Date, Time) VALUES (?, ?, ?, ?, ?, ?)"

    cursor.execute(f"SELECT * FROM {tablename}")

    fetch =  cursor.fetchall()

    budget = fetch[-1][3]
    
    withdraw = withdraw

    left = int(budget) - int(withdraw)

    withdrawal_purpose = purpose

    make_an_entry_args = (budget, withdraw, left, withdrawal_purpose, date, time)

    make_an_entry = cursor.execute(make_an_entry_query, make_an_entry_args)

    db.commit()

    return withdrawal_purpose


def db_budget_update(tablename, new_sources, added_budget):
    
    # afunction for the budget update mode of two parts the first to update the budget
    added_budget = int(added_budget)

    count_query = f"SELECT COUNT(*) FROM {tablename};"

    cursor.execute(count_query)

    fetch =  cursor.fetchall()

    count_fetch = fetch[0][0]

    for row in range(count_fetch):

        cursor.execute(f"SELECT * FROM {tablename}")

        fetch =  cursor.fetchall()

        old_budget = fetch[row][1]
        old_left = fetch[row][3]
        

        new_budget = added_budget + old_budget
        new_left = added_budget + old_left

        if row == 0:
            old_purpose = str(fetch[0][4])
            new_purpose = old_purpose + "+" + new_sources
            update_query = f"UPDATE {tablename} SET Budget = ?, Amount_left = ?, Withdrawal_purpose = ? WHERE id = {row+1};"
            update_args = (new_budget, new_left, new_purpose)

        elif row > 0:
            update_query = f"UPDATE {tablename} SET Budget = ?, Amount_left = ? WHERE id = {row+1};"
            update_args = (new_budget, new_left)

        cursor.execute(update_query, update_args)
        

        db.commit()

    # the second part of the function is to add an entry for the table with 
    # the amount, time and date of the budget update

    make_an_entry_query = f"INSERT INTO {tablename} (Budget, Withdraw, Amount_left, Withdrawal_purpose, Date, Time) VALUES (?, ?, ?, ?, ?, ?)"

    cursor.execute(f"SELECT * FROM {tablename}")

    fetch =  cursor.fetchall()

    budget = fetch[-1][3]

    withdraw = 0

    left = budget

    withdrawal_purpose = f"A budget update ({added_budget}) happened on:"

    make_an_entry_args = (budget, withdraw, left, withdrawal_purpose, date, time)

    make_an_entry = cursor.execute(make_an_entry_query, make_an_entry_args)

    db.commit()

    return new_purpose



def db_generate_report(tablename):

    count_query = f"SELECT * FROM {tablename};"

    cursor.execute(count_query)

    fetch =  cursor.fetchall()

    with open(f"{tablename}.csv", "a", newline="") as csvfile:
        headers = [
            "Budget",
            "Withdraw",
            "Amount_left",
            "Withdrawal_purpose",
            "Date",
            "Time",
        ]

        csv_out=csv.writer(csvfile)
        csv_out.writerow(headers)
        for row in fetch:
            csv_out.writerow(row)
 
    generate_report(f"{tablename}.csv")


def db_currency_update(tablename, currency):
    
    make_an_entry_query = f"INSERT INTO {tablename} (Budget, Withdraw, Amount_left, Withdrawal_purpose, Date, Time) VALUES (?, ?, ?, ?, ?, ?)"

    cursor.execute(f"SELECT * FROM {tablename}")

    fetch =  cursor.fetchall()

    budget = fetch[-1][3]

    withdraw = 0

    left = budget

    withdrawal_purpose = f"A currency update to ({currency}) happened on:"

    make_an_entry_args = (budget, withdraw, left, withdrawal_purpose, date, time)

    make_an_entry = cursor.execute(make_an_entry_query, make_an_entry_args)

    db.commit()

