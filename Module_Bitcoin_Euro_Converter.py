from forex_python.bitcoin import BtcConverter

btc = BtcConverter()

while True:
    amount = input("Amount in Euro (enter 'q' to quit): ")
    if amount.lower() == 'q':
        break

    try:
        amount = float(amount)
        converted = btc.convert_btc_to_cur(amount, 'EUR')
        latest_price = btc.get_latest_price('EUR')

        print("-------------------------------------------")
        print(f"Latest price: 1 Euro = {latest_price} BTC")
        print(f"{amount} EURO = {converted} BTC")
        print("-------------------------------------------")

    except ValueError:
        print("Invalid input! Please enter a valid amount.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
