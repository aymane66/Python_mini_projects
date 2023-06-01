a = input("Insert the first number: ")
b = input("Insert the second number: ")

try:
    a = float(a)
    b = float(b)

    if a > b:
        print("Max: ", a)
    elif b > a:
        print("Max: ", b)
    else:
        print("The numbers inserted are equal.")

except ValueError:
    print("Invalid input. Please insert a numerical values.")
    