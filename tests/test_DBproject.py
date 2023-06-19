import pytest
import sys
sys.path.append("..")
from project.DBproject import db_first_entry, db_make_an_entry, db_budget_update, db_generate_report, db_check_existence


def main():
    test_db_first_entry()
    test_db_make_an_entry()
    test_db_budget_update()
    # test_db_generate_report()
    test_db_check_existence()


def test_db_first_entry():
    assert db_first_entry("beedoo", 10000, "bee") == 10000
    assert db_first_entry("beedo", 2000, "bee") == 2000
    assert db_first_entry("beedoo", 10000, "bee") == 10000


def test_db_make_an_entry():
    assert db_make_an_entry("beedoo", 100, "beee") == "beee"
    assert db_make_an_entry("beedoo", 400, "keee") == "keee"


def test_db_budget_update():
    assert db_budget_update("beedo", "investments", "2000") == "First entry budget source(s): bee+investments"
    assert db_budget_update("beedoo", "stuff", "200") == "First entry budget source(s): bee+stuff"


def test_db_generate_report():
    ...


def test_db_check_existence():
    assert db_check_existence("beedoo") == False
    assert db_check_existence("bee") == True


if __name__ == "__main__":
    main()