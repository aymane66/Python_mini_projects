print("---------- Number Divisors Finder ----------")

number = input("Number: ")

try:
    number = int(number)

    if number > 0:
        print(f"Divisors of number {number} are: ")
        for i in range(1, number + 1):
            if number % i == 0:
                print(i, end=" ")
    else:
        print("You need to insert a number higher than 0")

except ValueError:
    print("Invalid input. Please insert a number. ")