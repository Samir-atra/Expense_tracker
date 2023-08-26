import subprocess

def convert_currency(trans_from, trans_to, amount):


    x = subprocess.run(["bash", "utils/FX.sh", "{}".format(trans_from), "{}".format(trans_to)], capture_output=True)


    # to get the mid rate of the currency exchange
    transfer_rate = float(x.stdout.decode('utf-8').strip().split()[10].strip(","))
    # print("this is transfer rate",transfer_rate)
    new_amount = amount * transfer_rate
    # print(new_amount)
    return new_amount

convert_currency("EUR", "USD", 1)