temp = input("Insert Water temperature in C°: ")

try:
    temp = float(temp)

    if temp < 0:
        print("Solid")
    elif temp >= 100:
        print("Gas")
    else:
        print("Liquid")

except ValueError:
    print("Invalid input. Please insert a number.")