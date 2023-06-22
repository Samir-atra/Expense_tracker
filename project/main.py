# add the currency change and update feature.
# connect a currency exchange API even if (USD, EUR) only.

from DBproject import db_first_entry, db_make_an_entry, db_budget_update, db_generate_report, db_check_existence, db_currency_update
from CSVproject import csv_first_entry, csv_make_an_entry, csv_budget_update, csv_generate_report, csv_check_existence, csv_currency_update
from datetime import datetime
import os
import argparse
import sys
import utils.Gui as Gui
import utils.report_generator as rg 



def main():
   
   
    # parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", help="budget editing mode", action="store_true")
    parser.add_argument("-g", help="report generation mode", action="store_true")
    parser.add_argument("-c", help="custom filename mode")
    parser.add_argument("-cu", help="currncy update mode", action="store_true")
    args = parser.parse_args()
   
   
    _, type_question = Gui.gui_function(
        "Choose type",
        f"Please, select the data saving type and click submit (csv, database): ",
        "",
        "Submit",
        "Cancel",
        1,
    )

    # generate the default file name which is the current month and year
    month = datetime.now().strftime("%B_%Y")
    
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
        _, budget_sources = Gui.gui_function(
            "Budget_update",
            "New budget sources (usage: source1+source2+source3+...): ",
            "Added budget amount: ",
            "Submit",
            "Cancel",
            2,
        )
        globals()[f"{datatype}_budget_update"](file_name, budget_sources[0], budget_sources[1])
    # currency update command line argument
    elif args.cu:
        _, new_currency = Gui.gui_function(
            "Currency upddate",
            "New currency (usd/ eur):",
            "",
            "Submit",
            "Cancel",
            1,
        )
        globals()[f"{datatype}_currency_update"](file_name, new_currency[0])
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
            globals()[f"{datatype}_generate_report"](file_name)
        else:
            sys.exit()
    # default program execution
    else:
        if globals()[f"{datatype}_check_existence"](file_name):
            _, budget_sources = Gui.gui_function(
                "Budget",
                "The amount of money for the month: ",
                "Sources of the budget: ",
                "Submit",
                "Cancel",
                2,
            )
            _, currency = Gui.gui_function("", "Currency(usd/ eur): ", "", "Submit", "Cancel", 1)
            globals()[f"{datatype}_first_entry"](
                file_name, budget_sources[0], budget_sources[1], currency[0]
            )
            _, q = Gui.gui_function("", "Any entries now(y/n): ", "", "Submit", "Cancel", 1)
            if q[0] == "y" or q[0] == "Y" or q[0] == "yes" or q[0] == "Yes":
                _, withdraw_amount_purpose = Gui.gui_function(
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
            globals()[f"{datatype}_make_an_entry"](
                file_name, withdraw_amount_purpose[0], withdraw_amount_purpose[1]
            )


if __name__ == "__main__":
    main()
