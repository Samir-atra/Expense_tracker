"""converts an amount from one currency to another using the FXTradeAPI"""

import subprocess
import sys


def convert_currency(trans_from, trans_to, amount):
    """
    converts the currancy for the amount given

    Args:
        trans_from (str): the currency to convert
        trans_to (str): the currency to convert to
        amount (int): the amount to convert

    Returns:
        float: the converted amount
    """

    subprocess.run(["sudo", "apt-get", "install", "-y", "jq"], check=True)
    x = subprocess.run(
        ["bash", "utils/FX.sh", "{}".format(trans_from), "{}".format(trans_to)],
        capture_output=True,
    )
    # to get the mid rate of the currency exchange
    try:
        transfer_rate = float(x.stdout.decode("utf-8").strip().split()[10].strip(","))
    except ValueError:
        sys.exit("Please, update your FXAPI access token")
    new_amount = amount * transfer_rate

    return new_amount

if __name__ == "__main__":
    convert_currency("EUR", "USD", 1)
