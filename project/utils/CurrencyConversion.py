import freecurrencyapi
from Gui import gui_function


def main():
    _, currencies = gui_function(
    "Converter",
    "Currency to convert from: ",
    "Currency to convert to: ",
    "Submit",
    "Cancel",
    2,
    )
    _, amount = gui_function(
        "Amount",
        "Amount of the money to be converted: ",
        "",
        "Submit",
        "Cancel",
        1,
    )
    convert_currency(currencies[0], currencies[1], int(amount[0]))


def convert_currency(trans_from, trans_to, amount):

    client = freecurrencyapi.Client('API-key')

    transfer_rate = client.latest([f"{trans_from}"])["data"][f"{trans_to}"]

    new_amount = amount * transfer_rate
    print(new_amount)
    return new_amount


if __name__ == "__main__":
    main()