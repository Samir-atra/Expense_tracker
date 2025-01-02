"""
run the execution of the project    
"""

from datetime import datetime
import os
import argparse
import sys
from project.db_project import (
    db_first_entry,
    db_make_an_entry,
    db_budget_update,
    db_generate_report,
    db_check_existence,
    db_currency_update,
)
from project.csv_project import (
    csv_first_entry,
    csv_make_an_entry,
    csv_budget_update,
    csv_generate_report,
    csv_check_existence,
    csv_currency_update,
)
import project.utils.gui as gui
import utils.report_generator as rg
import utils.take_a_photo as tp


def main():
    """
    the main function for the project that handles the command
    line arguments and the default program execution
    """
    # parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", help="budget editing mode", action="store_true")
    parser.add_argument("-g", help="report generation mode", action="store_true")
    parser.add_argument("-c", help="custom filename mode")
    parser.add_argument("-cu", help="currncy update mode", action="store_true")
    args = parser.parse_args()

    _, type_question = gui.gui_function(
        "Choose type",
        "Please, select the data saving type and click submit (csv, database): ",
        "",
        "Submit",
        "Cancel",
        1,
    )

    # generate the default file name which is the current month and year
    date_time = datetime.now()
    month = date_time.strftime("%B_%Y")

    if type_question[0] == "database":
        datatype = "db"
        file_name = month
    elif type_question[0] == "csv":
        datatype = "csv"
        file_name = f"{month}.csv"

    # process the command line arguments
    # custom name command line argument
    if args.c:
        if datatype == "csv":
            file_name = f"{args.c}.csv"
        elif datatype == "db":
            file_name = args.c

    # budget editing command line argument
    if args.b:
        _, budget_sources = gui.gui_function(
            "Budget_update",
            "New budget sources (usage: source1+source2+source3+...): ",
            "Added budget amount: ",
            "Submit",
            "Cancel",
            2,
        )
        globals()[f"{datatype}_budget_update"](
            file_name, budget_sources[0], budget_sources[1]
        )
    # currency update command line argument
    elif args.cu:
        _, new_currency = gui.gui_function(
            "Currency upddate",
            "New currency:",
            "",
            "Submit",
            "Cancel",
            1,
        )
        globals()[f"{datatype}_currency_update"](file_name, new_currency[0])
    # report generation command line argument
    elif args.g:
        globals()[f"{datatype}_generate_report"](file_name)

    # default program execution
    else:
        if globals()[f"{datatype}_check_existence"](file_name):
            _, budget_sources = gui.gui_function(
                "Budget",
                "The amount of money for the month: ",
                "Sources of the budget: ",
                "Submit",
                "Cancel",
                2,
            )
            _, currency = gui.gui_function("", "Currency: ", "", "Submit", "Cancel", 1)
            globals()[f"{datatype}_first_entry"](
                file_name, budget_sources[0], budget_sources[1], currency[0]
            )
            _, q = gui.gui_function(
                "", "Any entries now(y/n): ", "", "Submit", "Cancel", 1
            )
            if q[0] == "y" or q[0] == "Y" or q[0] == "yes" or q[0] == "Yes":
                _, withdraw_amount_purpose = gui.gui_function(
                    "Withdrawal",
                    "The amount to be withdrawn: ",
                    "The purpose of this withdrawal: ",
                    "Submit",
                    "Cancel",
                    2,
                )
                globals()[f"{datatype}_make_an_entry"](
                    file_name, withdraw_amount_purpose[0], withdraw_amount_purpose[1]
                )

                _, q = gui.gui_function(
                    "", "Any photos to take(y/n): ", "", "Submit", "Cancel", 1
                )
                if q[0] == "y" or q[0] == "Y" or q[0] == "yes" or q[0] == "Yes":
                    tp.capture()

            elif q[0] == "n" or q[0] == "N" or q[0] == "no" or q[0] == "No":
                pass
        else:
            _, withdraw_amount_purpose = gui.gui_function(
                "Withdrawal",
                "The amount to be withdrawn: ",
                "The purpose of this withdrawal: ",
                "Submit",
                "Cancel",
                2,
            )
            globals()[f"{datatype}_make_an_entry"](
                file_name, withdraw_amount_purpose[0], withdraw_amount_purpose[1]
            )

            _, q = gui.gui_function(
                "", "Any photos to take(y/n): ", "", "Submit", "Cancel", 1
            )
            if q[0] == "y" or q[0] == "Y" or q[0] == "yes" or q[0] == "Yes":
                tp.capture()


if __name__ == "__main__":
    main()
