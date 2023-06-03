number = input("Insert a number: ")

try:
    number = int(number)

    if number % 2 == 1:
        print("Odd number. ")
    else:
        print("Even number. ")

except ValueError:
    print("Invalid input. Please insert a number. ")