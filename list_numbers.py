number = input("Please insert a positive number: ")

try:
    number = int(number)
    if number < 0:
        print("Please insert a positive number!")
    else:
        numbers = list(range(1, number + 1))
        print("Numbers displayed:", numbers)

        even_numbers = list(range(2, number + 1, 2))
        print("Even numbers:", even_numbers)

        odd_numbers = list(range(1, number + 1, 2))
        print("Odd numbers:", odd_numbers)

except ValueError:
    print("Invalid input! Please insert a number.")
