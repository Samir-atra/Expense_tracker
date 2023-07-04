import freecurrencyapi


def main():
    trans_from = input("The curency to transfer from:")
    trans_to = input("The currency to transfer to:")
    amount = input("The amount of money to be transfered:")
    
    convert_currency(trans_from, trans_to, int(amount))


def convert_currency(trans_from, trans_to, amount):

    client = freecurrencyapi.Client("cgFct61Ju3nuTpM0Yv99JoxRgsLplbr2gsC9Nkvv")

    transfer_rate = client.latest([f"{trans_from}"])["data"][f"{trans_to}"]

    new_amount = amount * transfer_rate
    # print(new_amount)

    return new_amount


if __name__ == "__main__":
    main()
