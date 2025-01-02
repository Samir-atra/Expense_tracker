"""
check for the existance of the table for the month, create it if it does not exist, 
then make an entry to the database month table, and update the budget if needed,
generate a report for the month table, and update the currency if needed, 
"""

import sqlite3
from datetime import datetime
import csv
from project.utils.fx_trade import convert_currency
from utils.report_generator import (
    generate_report,
)  # this import must be commented for the tests to run.


# create constants and database cursor
DATABASE = "budgeting.db"
db = sqlite3.connect(DATABASE)
month = datetime.now().strftime("%B_%Y")
date = datetime.now().strftime("%x")
time = datetime.now().strftime("%X")

cursor = db.cursor()


def db_check_existence(tablename):
    """
    check the existance of a table in the budgeting database
    Args:
        tablename: the name of the table to be checked
    Returns:
        True if the table does not exist, False otherwise
    """
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
    """
    create a first entry to the table and create the table if it does not exists
    Args:
        tablename: the name of the table to be created
        budget: the initial budget of the month
        sources: the sources of the budget
        currency: the currency of the budget
    Returns:
        the budget of the month
    """
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
    """
    make an entry to the table in the budgeting database
    Args:
        tablename: the name of the table to be edited
        withdraw: the amount of money to be withdrawn
        purpose: the purpose of the withdrawal
    Returns:
        withdrawal_purpose: the purpose of the withdrawal
    """
    make_an_entry_query = f"INSERT INTO {tablename} (Budget, Withdraw, Amount_left, Withdrawal_purpose, Date, Time, Currency) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(f"SELECT * FROM {tablename}")
    fetch = cursor.fetchall()
    budget = fetch[-1][3]
    withdraw = withdraw
    left = int(budget) - int(withdraw)
    withdrawal_purpose = purpose
    currency = fetch[-1][7]
    make_an_entry_args = (
        budget,
        withdraw,
        left,
        withdrawal_purpose,
        date,
        time,
        currency,
    )
    make_an_entry = cursor.execute(make_an_entry_query, make_an_entry_args)
    db.commit()

    return withdrawal_purpose


def db_budget_update(tablename, new_sources, added_budget):
    """
    update the budget by the amount in added_budget
    Args:
        tablename: the name of the table to be edited
        new_sources: the sources of the new budget
        added_budget: the amount of money to be added to the budget
    Returns:
        make_an_entry_args: the arguments of the new entry
    """
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
    withdrawal_purpose = (
        f"A budget update ({added_budget} from {new_sources}) happened on:"
    )
    make_an_entry_args = (
        new_budget,
        withdraw,
        new_left,
        withdrawal_purpose,
        date,
        time,
        currency,
    )
    make_an_entry = cursor.execute(make_an_entry_query, make_an_entry_args)
    db.commit()

    return make_an_entry_args


def db_generate_report(tablename):
    """
    report generation for a database table.
    Args:
        tablename: the name of the table to be reported
    """
    count_query = f"SELECT * FROM {tablename};"
    cursor.execute(count_query)
    fetch = cursor.fetchall()
    with open(f"{tablename}.csv", "a", newline="", encoding = "utf-8") as csvfile:
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
    """
    currency update for a table in a database
    Args:
        tablename: the name of the table to be updated
        new_currency: the new currency to be updated
    """
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
        update_args = (
            f"{new_budget:.2f}",
            f"{new_withdraw:.2f}",
            f"{new_left:.2f}",
            new_currency,
        )
        cursor.execute(update_query, update_args)
        db.commit()
    make_an_entry_query = f"INSERT INTO {tablename} (Budget, Withdraw, Amount_left, Withdrawal_purpose, Date, Time, Currency) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(f"SELECT * FROM {tablename}")
    fetch = cursor.fetchall()
    budget = fetch[-1][1]
    withdraw = 0
    left = fetch[-1][3]
    withdrawal_purpose = (
        f"A currency update from {old_currency} to {new_currency} happened on:"
    )
    make_an_entry_args = (
        budget,
        withdraw,
        left,
        withdrawal_purpose,
        date,
        time,
        new_currency,
    )
    make_an_entry = cursor.execute(make_an_entry_query, make_an_entry_args)
    db.commit()
