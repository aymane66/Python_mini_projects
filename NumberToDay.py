n = input("Insert a number from 1 to 7: ")

try:
    n = int(n)

    if n == 1:
        print("Sunday")
    elif n == 2:
        print("Monday")
    elif n == 3:
        print("Tuesday")
    elif n == 4:
        print("Wednesday")
    elif n == 5:
        print("Thursday")
    elif n == 6:
        print("Friday")
    elif n == 7:
        print("Saturday")
    else:
        print("Invalid number. Enter a number between 1 and 7")

except ValueError:
    print("Error. Please insert a number.")
