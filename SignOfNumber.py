n = input("Insert a number: ")

try:
    n = float(n)

    if n < 0:
        print("Negative number.")
    elif n > 0:
        print("Positive number.")
    else:
        print("Null.")

except ValueError:
    print("Error. Please insert a numerical input. ")