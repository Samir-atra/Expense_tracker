import pytest
import sys
sys.path.append("..")
from project.utils import Gui
from project.utils import report_generator
from project.CSVproject import csv_first_entry, csv_make_an_entry, csv_budget_update, csv_generate_report, csv_check_existence
from project.DBproject import db_first_entry, db_make_an_entry, db_budget_update, db_generate_report, db_check_existence


def main():
    test_csv_first_entry()
    # test_csv_make_an_entry()
    test_csv_budget_update()
    # test_csv_generate_report()
    # test_csv_check_existence()


def test_csv_first_entry():
    assert csv_first_entry("beedoo.csv", 10000, "bee") == 10000
    assert csv_first_entry("beedoo", 2000, "bee") == 2000


def test_csv_make_an_entry():
    assert csv_make_an_entry("beedoo", 100, "beee") == "beee"
    assert csv_make_an_entry("beedoo", 400, "keee") == "keee"


def test_csv_budget_update():
    print(csv_budget_update("beedoo.csv", "inve", "2000"))


main()
