number = input("Insert a number: ")

try:
    number = int(number)

    r = number % 2

    if r == 1:
        print("Odd number. ")
    else:
        print("Even number. ")

except ValueError:
    print("Invalid input. Please insert a number. ")