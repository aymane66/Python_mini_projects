number = input("Insert a number: ")

try:
    number = int(number)

    if number % 2 == 1:
        print(number, "is an odd number. ")
    else:
        print(number, "is an even number. ")

except ValueError:
    print("Invalid input. Please insert a number. ")