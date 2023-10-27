# imports
import sqlite3
from datetime import datetime
import os
import time as tm
import argparse
import re
import sys
import csv
from utils.FXTrade import convert_currency
from utils.report_generator import (
    generate_report,
)  # this import must be commented for the tests to run.


Database = "budgeting.db"

db = sqlite3.connect(Database)

month = datetime.now().strftime("%B_%Y")

date = datetime.now().strftime("%x")
time = datetime.now().strftime("%X")

cursor = db.cursor()


def db_check_existence(tablename):

    check_exictance_query = (
        f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tablename}';"
    )

    check_query = cursor.execute(check_exictance_query)

    db.commit()

    fetch = cursor.fetchall()

    if fetch == []:
        return True
    else:
        return False


def db_first_entry(tablename, budget, sources, currency):

    create_table_query = f"CREATE TABLE IF NOT EXISTS {tablename} (Id INTEGER PRIMARY KEY AUTOINCREMENT, Budget INTEGER, Withdraw INTEGER, Amount_left INTEGER, Withdrawal_purpose TEXT, Date TEXT, Time TEXT, Currency TEXT)"

    create_table = cursor.execute(create_table_query)

    db.commit()

    budget = int(budget)

    sources = sources

    init_entry_query = f"INSERT INTO {tablename} (Budget, Withdraw, Amount_left, Withdrawal_purpose, Date, Time, Currency) VALUES (?, 0, ?, ?, ?, ?, ?);"

    init_entry_args = (
        budget,
        budget,
        f"First entry budget source(s): {sources}",
        date,
        time,
        currency,
    )

    init_entry = cursor.execute(init_entry_query, init_entry_args)

    db.commit()
    return budget


def db_make_an_entry(tablename, withdraw, purpose):

    make_an_entry_query = f"INSERT INTO {tablename} (Budget, Withdraw, Amount_left, Withdrawal_purpose, Date, Time, Currency) VALUES (?, ?, ?, ?, ?, ?, ?)"

    cursor.execute(f"SELECT * FROM {tablename}")

    fetch = cursor.fetchall()

    budget = fetch[-1][3]

    withdraw = withdraw

    left = int(budget) - int(withdraw)

    withdrawal_purpose = purpose
    currency = fetch[-1][7]
    make_an_entry_args = (budget, withdraw, left, withdrawal_purpose, date, time, currency)

    make_an_entry = cursor.execute(make_an_entry_query, make_an_entry_args)

    db.commit()

    return withdrawal_purpose


def db_budget_update(tablename, new_sources, added_budget):

    # a function for the budget update mode
    added_budget = int(added_budget)

    make_an_entry_query = f"INSERT INTO {tablename} (Budget, Withdraw, Amount_left, Withdrawal_purpose, Date, Time, Currency) VALUES (?, ?, ?, ?, ?, ?, ?)"

    cursor.execute(f"SELECT * FROM {tablename}")

    fetch = cursor.fetchall()

    old_budget = fetch[-1][1]
    old_left = fetch[-1][3]

    new_budget = added_budget + old_budget
    withdraw = 0
    new_left = added_budget + old_left
    currency = fetch[-1][7]
    withdrawal_purpose = f"A budget update ({added_budget} from {new_sources}) happened on:"

    make_an_entry_args = (new_budget, withdraw, new_left, withdrawal_purpose, date, time, currency)

    make_an_entry = cursor.execute(make_an_entry_query, make_an_entry_args)

    db.commit()

    return make_an_entry_args


def db_generate_report(tablename):

    count_query = f"SELECT * FROM {tablename};"

    cursor.execute(count_query)

    fetch = cursor.fetchall()

    with open(f"{tablename}.csv", "a", newline="") as csvfile:
        headers = [
            "Budget",
            "Withdraw",
            "Amount_left",
            "Withdrawal_purpose",
            "Date",
            "Time",
            "Currency",
        ]

        csv_out = csv.writer(csvfile)
        csv_out.writerow(headers)
        for row in fetch:
            csv_out.writerow(row[1:])


    generate_report(f"{tablename}.csv")


def db_currency_update(tablename, new_currency):

    cursor.execute(f"SELECT * FROM {tablename}")
    fetch = cursor.fetchall()
    old_currency = fetch[-1][7]
    if new_currency == old_currency:
        raise Exception("The file is already in the required currency")
    exchange_rate = convert_currency(old_currency, new_currency, 1)

    count_query = f"SELECT COUNT(*) FROM {tablename};"
    cursor.execute(count_query)
    countfetch = cursor.fetchall()
    count_fetch = countfetch[0][0]
    for row in range(count_fetch):

        cursor.execute(f"SELECT * FROM {tablename}")

        fetch = cursor.fetchall()

        old_budget = fetch[row][1]
        old_withdraw = fetch[row][2]
        old_left = fetch[row][3]

        new_budget = old_budget * exchange_rate
        new_withdraw = old_withdraw * exchange_rate
        new_left = old_left * exchange_rate

        
        update_query = f"UPDATE {tablename} SET Budget = ?, Withdraw = ?, Amount_left = ?, Currency = ? WHERE id = {row+1};"
        update_args = (f"{new_budget:.2f}", f"{new_withdraw:.2f}", f"{new_left:.2f}", new_currency)

        cursor.execute(update_query, update_args)

        db.commit()

    make_an_entry_query = f"INSERT INTO {tablename} (Budget, Withdraw, Amount_left, Withdrawal_purpose, Date, Time, Currency) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(f"SELECT * FROM {tablename}")
    fetch = cursor.fetchall()

    budget = fetch[-1][1]
    withdraw = 0
    left = fetch[-1][3]
    withdrawal_purpose = f"A currency update from {old_currency} to {new_currency} happened on:"

    make_an_entry_args = (budget, withdraw, left, withdrawal_purpose, date, time, new_currency)

    make_an_entry = cursor.execute(make_an_entry_query, make_an_entry_args)

    db.commit()
