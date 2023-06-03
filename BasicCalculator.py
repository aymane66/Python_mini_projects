x = input("x: ")
op = input("operator: ")
y = input("y: ")

try:
    x = float(x)
    y = float(y)

    if op == "+":
        r = x + y
        print("Result: ", format(r, ".2f"))
    elif op == "-":
        r = x - y
        print("Result: ", format(r, ".2f"))
    elif op == "*":
        r = x * y
        print("Result: ", format(r, ".2f"))
    elif op == "/":
        if y != 0:
            r = x / y
            print("Result: ", format(r, ".2f"))
        else:
            print("Error. Division by zero is not allowed.")
    else:
        print("Invalid operator. Please enter one of '+', '-', '*', or '/'.")

except ValueError:
    print("Invalid input. Please enter numbers for x and y.")
