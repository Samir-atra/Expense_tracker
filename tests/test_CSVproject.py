import pytest
import sys
sys.path.append("..")
from project.utils import Gui
from project.utils import report_generator
from project.CSVproject import csv_first_entry, csv_make_an_entry, csv_budget_update, csv_generate_report, csv_check_existence


def main():
    test_csv_first_entry()
    test_csv_make_an_entry()
    test_csv_budget_update()
    # test_csv_generate_report()
    test_csv_check_existence()


def test_csv_first_entry():
    assert csv_first_entry("beedoo.csv", 10000, "bee") == 10000
    assert csv_first_entry("beedo.csv", 2000, "bee") == 2000
    assert csv_first_entry("beedoo", 10000, "bee") == 10000


def test_csv_make_an_entry():
    assert csv_make_an_entry("beedoo", 100, "beee") == "beee"
    assert csv_make_an_entry("beedoo", 400, "keee") == "keee"


def test_csv_budget_update():
    assert csv_budget_update("beedoo.csv", "investments", "2000") == "First entry budget source(bee+investments)"
    assert csv_budget_update("beedo.csv", "stuff", "200") == "First entry budget source(bee+stuff)"


def test_csv_generate_report():
    ...


def test_csv_check_existence():
    assert csv_check_existence("beedoo.csv") == False
    assert csv_check_existence("bee.csv") == True


if __name__ == "__main__":
    main()
