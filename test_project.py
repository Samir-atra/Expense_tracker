from project import create_csv_file_for_the_month, make_an_entry, budget_update


def main():
    test_create_csv_file_for_the_month()
    test_make_an_entry()
    test_budget_update()


def test_create_csv_file_for_the_month():
    assert create_csv_file_for_the_month("file.csv", "10000", "salary") == "10000"
    assert create_csv_file_for_the_month("filey.csv", "20000", "salary") == "20000"


def test_make_an_entry():
    assert make_an_entry("file.csv", "100", "buy a car") == "buy a car"
    assert make_an_entry("filey.csv", "200", "buy a plane") == "buy a plane"


def test_budget_update():
    assert (
        budget_update("file.csv", "investment", "3000")
        == "First entry budget source(salary+investment)"
    )
    assert (
        budget_update("filey.csv", "sold goods", "3000")
        == "First entry budget source(salary+sold goods)"
    )
