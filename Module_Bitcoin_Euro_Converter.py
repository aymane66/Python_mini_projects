from currency_converter import CurrencyConverter

amount = input("Amount in BitCoin: ")

try:
    amount = float(amount)

    R = CurrencyConverter.convert(amount, 'EUR', 'USD')

    print(R)

except ValueError:
    print("Invalid input! ")