x = input("Insert the first number: ")
y = input("Insert the second number: ")

try:
    x = float(x)
    y = float(y)

    if (x < 0 and y < 0) or (x > 0 and y > 0):
        print("Same sign. ")
    else:
        print("Different signs. ")

except ValueError:
    print("Error. Please insert numerical values. ")


