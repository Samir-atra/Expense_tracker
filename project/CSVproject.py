# expense tracker project

"""
what I want to build is a program that

take in: - the month budget
         - amount withdrawn each time
         - the reason for withdrawal
         - (might add a "user" later)

give out in a .csv file named "current month and year": - the month budget
                                                        - the amount withdrawn
                                                        - the amount left from the budget
                                                        - the reason for withdrawal
                                                        - date of the withdrawal
                                                        - time of the withdrawal

featues to be added:
- The ability to update the month budget in the middle of the month
- the ability to have a full track for the inputs and outputs has been added and removed from the project for the current month(concat everything in one pdf file)
- the ability to custom name the files.
- the ability to include reciept images and checks in the report file.

Exceptions to be added:
- filling a single bar in a two bar window. DONE
- entering a none csv filename in -c mode. DONE
- withdrawing more than the amount left in the budget.  DONE
- using c mode without a filename. DONE
- adding a budget source without a plus sign. Done
- add the ability to save the info in a database to the side of a csv file.

check the rest file for improvements

"""

# imports
from datetime import datetime
import csv
import pandas as pd
import os
import time as tm
import argparse
import re
import sys
import utils.Gui as Gui
import utils.report_generator as rg 


def main():
    # parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", help="budget editing mode", action="store_true")
    parser.add_argument("-g", help="report generation mode", action="store_true")
    parser.add_argument("-c", help="custom csv filename mode")
    args = parser.parse_args()

    # generate the default file name which is the current month and year
    month = datetime.now().strftime("%B_%Y")
    file_name = str(f"{month}.csv")

    # process the command line arguments
    # custom name command line argument
    if args.c:
        if ".csv" not in args.c:
            sys.exit("Invalid filename")
        else:
            file_name = args.c
    # budget editing command line argument
    if args.b:
        _, budget_sources = Gui.gui_function(
            "Budget_update",
            "New budget sources (usage: source1+source2+source3+...): ",
            "Added budget amount: ",
            "Submit",
            "Cancel",
            2,
        )
        budget_update(file_name, budget_sources[0], budget_sources[1])
    # report generation command line argument
    elif args.g:
        d = os.getcwd()
        _, question = Gui.gui_function(
            "Question",
            f"Please, add any images (use extension: .jpg or .png) related to the report you are trying to generate in the directory: {d}, Continue(y/n): ",
            "",
            "Submit",
            "Cancel",
            1,
        )
        if (
            question[0] == "y"
            or question[0] == "yes"
            or question[0] == "Yes"
            or question[0] == "Y"
        ):
            rg.generate_report(file_name)
        else:
            sys.exit()
    # default program execution
    else:
        if file_name not in os.listdir():
            _, budget_sources = Gui.gui_function(
                "Budget",
                "The amount of money for the month: ",
                "Sources of the budget: ",
                "Submit",
                "Cancel",
                2,
            )
            create_csv_file_for_the_month(
                file_name, budget_sources[0], budget_sources[1]
            )
            _, q = Gui.gui_function("", "Any entries now(y/n): ", "", "Submit", "Cancel", 1)
            if q[0] == "y" or q[0] == "Y" or q[0] == "yes" or q[0] == "Yes":
                _, withdraw_amount_purpose = gui_function(
                    "Withdrawal",
                    "The amount to be withdrawn: ",
                    "The purpose of this withdrawal: ",
                    "Submit",
                    "Cancel",
                    2,
                )
                make_an_entry(
                    file_name, withdraw_amount_purpose[0], withdraw_amount_purpose[1]
                )

            elif q[0] == "n" or q[0] == "N" or q[0] == "no" or q[0] == "No":
                pass
        else:
            _, withdraw_amount_purpose = Gui.gui_function(
                "Withdrawal",
                "The amount to be withdrawn: ",
                "The purpose of this withdrawal: ",
                "Submit",
                "Cancel",
                2,
            )
            make_an_entry(
                file_name, withdraw_amount_purpose[0], withdraw_amount_purpose[1]
            )


def create_csv_file_for_the_month(file_name, budget, sources):
    # a function to initiate a csv file and write the first line of it
    print("Creating file...")
    tm.sleep(2)
    withdraw = 0
    purpose = "First entry budget source ({})".format(sources)
    dicti = Dictionary()
    dic = dicti.update(budget, withdraw, purpose)
    the_writer(file_name, dic, True)

    return dic[0]["Budget"]


def make_an_entry(file_name, withdraw, purpose):
    # a function to edit the csv file and add withdrawal lines to it
    with open(file_name, "r") as file:
        data = file.readlines()
        lastRow = data[-1]
        l = lastRow.split(",")
        budget = l[2]
    dicti = Dictionary()
    dic = dicti.update(budget, withdraw, purpose)
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
        ]
        csvwriter = csv.DictWriter(csvfile, fieldnames=headers)
        if type:
            csvwriter.writeheader()
        csvwriter.writerows(dic)
    return True


def budget_update(file_name, new_sources, added_budget):
    # a function to make the necessary edits to the csv file when a budget edit is needed
    x = pd.DataFrame(pd.read_csv(file_name))
    old_sources = re.search("\(([a-zA-Z+ ]*)\)", x.at[0, "Withdrawal_purpose"])
    try:
        x.at[0, "Withdrawal_purpose"] = "First entry budget source({}+{})".format(
            old_sources[1], new_sources
        )
    except TypeError:
        sys.exit("Please, edit the csv file manually to match the correct usage.")

    x.Budget = x.Budget + int(added_budget)
    x.Amount_left = x.Amount_left + int(added_budget)
    dicti = Dictionary()
    dic = dicti.budg_up(x.iloc[-1, 0], x.iloc[-1, 2])
    df = pd.DataFrame(dic, index=["Time"])
    x = pd.concat([x, df], ignore_index=True)
    x.to_csv(file_name, index=False)

    return x.at[0, "Withdrawal_purpose"]


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
            }
        ]
        self.date = datetime.now().strftime("%x")
        self.time = datetime.now().strftime("%X")

    def update(self, budget, withdraw, purpose):
        self.di[0]["Budget"] = budget
        self.di[0]["Withdraw"] = withdraw
        try:
            left = int(budget) - int(withdraw)
        except ValueError:
            sys.exit("Invalid input.")
        if left < 0:
            raise Exception("You do not have that amount left in the budget.")
        self.di[0]["Amount_left"] = str(left)
        self.di[0]["Withdrawal_purpose"] = purpose
        self.di[0]["Date"] = self.date
        self.di[0]["Time"] = self.time

        return self.di

    def budg_up(self, budget, amount_left):
        self.di[0]["Budget"] = budget
        self.di[0]["Withdraw"] = 0
        self.di[0]["Amount_left"] = amount_left
        self.di[0]["Withdrawal_purpose"] = "A budget update happened on: "
        self.di[0]["Date"] = self.date
        self.di[0]["Time"] = self.time

        return self.di


if __name__ == "__main__":
    main()
