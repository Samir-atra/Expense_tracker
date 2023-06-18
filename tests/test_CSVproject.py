import pytest
import sys
sys.path.append("..")
from project.utils import Gui
from project.utils import report_generator
from project.CSVproject import csv_first_entry

def main():
    test_csv_first_entry()
    # test_csv_make_an_entry()
    # test_csv_budget_update()
    # test_csv_generate_report()
    # test_csv_check_existence()


def test_csv_first_entry():
    print(csv_first_entry("beedoo", 10000, "bee"))

main()
