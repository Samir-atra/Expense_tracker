"""
checks the existence of a csv file, and in case it does not 
initiates a csv file, makes an entry to a month budget csv 
file, updates the budget in a csv file, and generates a report 
from a month budget csv file. and creat a dictionary object to 
use for updating and creating the csv file
"""

from datetime import datetime
import csv
import os
import sys
import pandas as pd
from utils.report_generator import (
    generate_report,
)  # this import must be commented for the tests modules to run.
from project.utils.fx_trade import convert_currency


def csv_check_existence(filename):
    """
    check if the file already exists or needs to be created
    Args:
        filename: the name of the file to be checked
    Returns:
        True if the file does not exist, False otherwise
    """
    if filename not in os.listdir():
        return True
    else:
        return False


def csv_first_entry(file_name, budget, sources, currency):
    """
    initiate a csv file and write the first line of it
    Args:
        file_name: the name of the file to be created
        budget: the initial budget of the month
        sources: the sources of the budget
        currency: the currency of the budget
    Returns:
        the budget of the month
    """
    withdraw = 0
    purpose = f"First entry budget source ({sources})"
    dicti = Dictionary()
    dic = dicti.entry(budget, withdraw, purpose, currency)
    the_writer(file_name, dic, True)

    return dic[0]["Budget"]


def csv_make_an_entry(file_name, withdraw, purpose):
    """
    edit the csv file and add withdrawal lines to it
    Args:
        file_name: the name of the file to be edited
        withdraw: the amount of money to be withdrawn
        purpose: the purpose of the withdrawal
    Returns:
        the purpose of the withdrawal
    """
    with open(file_name, "r", encoding="utf-8") as file:
        data = file.readlines()
        last_row = data[-1]
        l = last_row.split(",")
        budget = l[2]
        currency = l[6].strip()
    dicti = Dictionary()
    dic = dicti.entry(budget, withdraw, purpose, currency)
    the_writer(file_name, dic, False)

    return dic[0]["Withdrawal_purpose"]


def the_writer(file_name, dic, entry_type):
    """
    write the data generate in the "create_csv_file_for_the_month" and "make_an_entry"
    into the csv file.
    Args:
        file_name: the name of the file to be written
        dic: the dictionary object as defined below to be written
        type: the type of the writing wheter it is the first entry in the month or not
    Returns:
        True if the writing is successful, False otherwise
    """
    with open(file_name, "a", newline="", encoding="utf-8") as csvfile:
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
        if entry_type:
            csvwriter.writeheader()
        csvwriter.writerows(dic)
    return True


def csv_budget_update(file_name, new_sources, added_budget):
    """
    make the necessary edits to the csv file when a budget edit is needed
    Args:
        file_name: the name of the file to be edited
        new_sources: the new sources of the budget to be added
        added_budget: the amount of money to be added to the budget
    Returns:
        the dictionary object as defined below
    """
    with open(file_name, "r", encoding="utf-8") as file:
        data = file.readlines()
        last_row = data[-1]
        l = last_row.split(",")
        budget = float(l[2]) + float(added_budget)
        amount_left = budget
        withdrawal_purpose = (
            f"A budget update ({added_budget} from {new_sources}) happened on: "
        )
        currency = l[6].strip()
        dicti = Dictionary()
        dic = dicti.update(budget, amount_left, withdrawal_purpose, currency)
        the_writer(file_name, dic, False)

        return dic


def csv_generate_report(file_name):
    """rename the generate report function to be used in the csv module
    Args:
        file_name: the name of the file to be reported
    """
    generate_report(file_name)


def csv_currency_update(file_name, new_currency):
    """
    deliver the currency update of the currency update mode on csv data files
    Args:
        file_name: the name of the file to be updated
        new_currency: the new currency to be updated
    """
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
    dic = dicti.update(
        f"{x.iloc[-1, 0]:.2f}",
        f"{x.iloc[-1, 2]:.2f}",
        f"A currency update from {old_currency} to ({new_currency}) happened on: ",
        new_currency,
    )
    df = pd.DataFrame(dic, index=["Time"])
    x = pd.concat([x, df], ignore_index=True)
    x.to_csv(file_name, index=False)


class Dictionary:
    """
    a class with the dictionary forms needed in the code above
    """

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

    def entry(self, budget, withdraw, purpose, currency):
        """
        a help function to make an entry to a csv file
        Args:
            budget: the budget of the month
            withdraw: the amount of money to be withdrawn
            purpose: the purpose of the withdrawal
            currency: the currency of the budget
        Returns:
            the dictionary object as defined below
        """
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
        """a help function to deliver a currency or a budget update.
        Args:
            budget: the budget of the month
            amount_left: the amount of money left in the budget
            purpose: the purpose of the withdrawal
            currency: the currency of the budget
        Returns:
            the dictionary object as defined below
        """
        self.di[0]["Budget"] = budget
        self.di[0]["Withdraw"] = 0
        self.di[0]["Amount_left"] = amount_left
        self.di[0]["Withdrawal_purpose"] = purpose
        self.di[0]["Date"] = self.date
        self.di[0]["Time"] = self.time
        self.di[0]["Currency"] = currency

        return self.di
