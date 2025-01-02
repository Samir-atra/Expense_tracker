"""
test module for the db_project module functions
"""

import sys
from project.db_project import (
    db_first_entry,
    db_make_an_entry,
    db_budget_update,
    db_check_existence,
)
import pytest

sys.path.append("..")


def main():
    """
    the main function for the test module
    """
    test_db_first_entry()
    test_db_make_an_entry()
    test_db_budget_update()
    test_db_check_existence()


def test_db_first_entry():
    """
    test the db first entry function
    """
    assert db_first_entry("beedoo", 10000, "bee") == 10000
    assert db_first_entry("beedo", 2000, "bee") == 2000
    assert db_first_entry("beedoo", 10000, "bee") == 10000


def test_db_make_an_entry():
    """
    test the db make an entry function
    """
    assert db_make_an_entry("beedoo", 100, "beee") == "beee"
    assert db_make_an_entry("beedoo", 400, "keee") == "keee"


def test_db_budget_update():
    """
    test the db budget update function
    """
    assert (
        db_budget_update("beedo", "investments", "2000")
        == "First entry budget source(s): bee+investments"
    )
    assert (
        db_budget_update("beedoo", "stuff", "200")
        == "First entry budget source(s): bee+stuff"
    )


def test_db_check_existence():
    """
    test the db check existence function
    """
    assert db_check_existence("beedoo") is False
    assert db_check_existence("bee") is True


if __name__ == "__main__":
    main()
