n = 0

while n <= 10 or n >= 20:
    try:
        n = int(input("Numbers (between 10 and 20): "))
        if n >= 20:
            print("Too big! Please enter a smaller number. ")
        elif n <= 10:
            print("Too small! Please enter a larger number. ")
        else:
            print("Congrats! You chose a number between 10 and 20. ")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
