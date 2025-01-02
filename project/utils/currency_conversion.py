"""
converts the current currancy to another for the given amount 
using the freecurranceapi library
"""

import freecurrencyapi


def main():
    """
    takes user input and call the convert_currency function
    """
    trans_from = input("The curency to transfer from:")
    trans_to = input("The currency to transfer to:")
    amount = input("The amount of money to be transfered:")

    convert_currency(trans_from, trans_to, int(amount))


def convert_currency(trans_from, trans_to, amount):
    """
    call the freecurrancyapi and convert for the amount given

    Args:
        trans_from (str): the currency to transfer from
        trans_to (str): the currency to transfer to
        amount (int): the amount to be transfered

    Returns:
        new_amount (float): the new amount after the conversion
    """

    client = freecurrencyapi.Client("<client API>")
    transfer_rate = client.latest([f"{trans_from}"])["data"][f"{trans_to}"]
    new_amount = amount * transfer_rate

    return new_amount


if __name__ == "__main__":
    main()
