"""
test for the csv_project module functions
"""
import sys
import pytest
sys.path.append("..")
from project.utils import gui
from project.utils import report_generator
from project.csv_project import (
    csv_first_entry,
    csv_make_an_entry,
    csv_budget_update,
    csv_generate_report,
    csv_check_existence,
)


def main():
    """the main function for the test module"""
    test_csv_first_entry()
    test_csv_make_an_entry()
    test_csv_budget_update()
    # test_csv_generate_report()
    test_csv_check_existence()


def test_csv_first_entry():
    """
    test the csv first entry function
    """
    assert csv_first_entry("beedoo.csv", 10000, "bee") == 10000
    assert csv_first_entry("beedo.csv", 2000, "bee") == 2000
    assert csv_first_entry("beedoo", 10000, "bee") == 10000


def test_csv_make_an_entry():
    """
    test the csv make an entry function
    """
    assert csv_make_an_entry("beedoo", 100, "beee") == "beee"
    assert csv_make_an_entry("beedoo", 400, "keee") == "keee"


def test_csv_budget_update():
    """
    test the csv budget update function
    """
    assert (
        csv_budget_update("beedoo.csv", "investments", "2000")
        == "First entry budget source(bee+investments)"
    )
    assert (
        csv_budget_update("beedo.csv", "stuff", "200")
        == "First entry budget source(bee+stuff)"
    )


def test_csv_check_existence():
    """
    test the csv check existence function
    """
    assert csv_check_existence("beedoo.csv") is False
    assert csv_check_existence("bee.csv") is True


if __name__ == "__main__":
    main()
