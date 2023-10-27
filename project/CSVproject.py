# imports
from datetime import datetime
import csv
import pandas as pd
import os
import time as tm
import argparse
import re
import sys
from utils.report_generator import (
    generate_report,
)  # this import must be commented for the tests to run.
from utils.FXTrade import convert_currency


def csv_check_existence(filename):
    # check if the file already exists or must be created
    if filename not in os.listdir():
        return True
    else:
        return False


def csv_first_entry(file_name, budget, sources, currency):
    # a function to initiate a csv file and write the first line of it
    withdraw = 0
    purpose = f"First entry budget source ({sources})"
    dicti = Dictionary()
    dic = dicti.entry(budget, withdraw, purpose, currency)
    the_writer(file_name, dic, True)

    return dic[0]["Budget"]


def csv_make_an_entry(file_name, withdraw, purpose):
    # a function to edit the csv file and add withdrawal lines to it
    with open(file_name, "r") as file:
        data = file.readlines()
        lastRow = data[-1]
        l = lastRow.split(",")
        budget = l[2]
        currency = l[6].strip()
    dicti = Dictionary()
    dic = dicti.entry(budget, withdraw, purpose, currency)
    the_writer(file_name, dic, False)

    return dic[0]["Withdrawal_purpose"]


def the_writer(file_name, dic, type):
    # a function to write the data generate in the "create_csv_file_for_the_month" and "make_an_entry" into the csv file.
    with open(file_name, "a", newline="") as csvfile:
        headers = [
            "Budget",
            "Withdraw",
            "Amount_left",
            "Withdrawal_purpose",
            "Date",
            "Time",
            "Currency",
        ]
        csvwriter = csv.DictWriter(csvfile, fieldnames=headers)
        if type:
            csvwriter.writeheader()
        csvwriter.writerows(dic)
    return True


def csv_budget_update(file_name, new_sources, added_budget):
    # a function to make the necessary edits to the csv file when a budget edit is needed
     with open(file_name, "r") as file:
        data = file.readlines()
        lastRow = data[-1]
        l = lastRow.split(",")
        budget = float(l[2]) + float(added_budget)
        amount_left = budget
        withdrawal_purpose = f"A budget update ({added_budget} from {new_sources}) happened on: "
        currency = l[6].strip()
        dicti = Dictionary()
        dic = dicti.update(budget, amount_left, withdrawal_purpose, currency)
        the_writer(file_name, dic, False)

        return dic


def csv_generate_report(file_name):
    generate_report(file_name)


def csv_currency_update(file_name, new_currency):

    x = pd.DataFrame(pd.read_csv(file_name))
    old_currency = x.iloc[-1, 6]
    if new_currency == old_currency:
        raise Exception("The file is already in the required currency")
    exchange_rate = convert_currency(old_currency, new_currency, 1)
    exchange_rate = "{:.2f}".format(exchange_rate)
    x.Budget = x.Budget * float(exchange_rate)
    x.Withdraw = x.Withdraw * float(exchange_rate)
    x.Amount_left = x.Amount_left * float(exchange_rate)
    x.Currency = new_currency
    dicti = Dictionary()
    dic = dicti.update(f"{x.iloc[-1, 0]:.2f}", f"{x.iloc[-1, 2]:.2f}", f"A currency update from {old_currency} to ({new_currency}) happened on: ", new_currency)
    df = pd.DataFrame(dic, index=["Time"])
    x = pd.concat([x, df], ignore_index=True)
    x.to_csv(file_name, index=False)


class Dictionary:
    # a class with the dictionary forms needed in the code above
    def __init__(self):
        self.di = [
            {
                "Budget": 0,
                "Withdraw": 0,
                "Amount_left": 0,
                "Withdrawal_purpose": "",
                "Date": "",
                "Time": "",
                "Currency": "",
            }
        ]
        self.date = datetime.now().strftime("%x")
        self.time = datetime.now().strftime("%X")

    def entry(self, budget, withdraw,  purpose, currency):
        self.di[0]["Budget"] = budget
        self.di[0]["Withdraw"] = withdraw
        try:
            left = float(budget) - float(withdraw)
        except ValueError:
            sys.exit("Invalid input.")
        if left < 0:
            raise Exception("You do not have that amount left in the budget.")
        self.di[0]["Amount_left"] = str(left)
        self.di[0]["Withdrawal_purpose"] = purpose
        self.di[0]["Date"] = self.date
        self.di[0]["Time"] = self.time
        self.di[0]["Currency"] = currency

        return self.di

    def update(self, budget, amount_left, purpose, currency):
        self.di[0]["Budget"] = budget
        self.di[0]["Withdraw"] = 0
        self.di[0]["Amount_left"] = amount_left
        self.di[0]["Withdrawal_purpose"] = purpose
        self.di[0]["Date"] = self.date
        self.di[0]["Time"] = self.time
        self.di[0]["Currency"] = currency

        return self.di
