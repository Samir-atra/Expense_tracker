import subprocess
import sys

def convert_currency(trans_from, trans_to, amount):

    subprocess.run(["sudo", "apt-get", "install", "-y", "jq"], check=True)
    x = subprocess.run(["bash", "utils/FX.sh", "{}".format(trans_from), "{}".format(trans_to)], capture_output=True)

    # to get the mid rate of the currency exchange
    try:
        transfer_rate = float(x.stdout.decode('utf-8').strip().split()[10].strip(","))
    except ValueError:
        sys.exit("Please, update your FXAPI access token")
    # print("this is transfer rate",transfer_rate)
    new_amount = amount * transfer_rate
    # print(new_amount)
    return new_amount

convert_currency("EUR", "USD", 1)