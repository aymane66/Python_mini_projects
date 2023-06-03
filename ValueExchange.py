x = input("Insert the first number: ")
y = input("Insert the second nuber: ")

try:
    x = float(x)
    y = float(y)

    # if same sign, we exchange value
    if (x < 0 and y < 0) or (x > 0 and y > 0):
        temp = x
        x = y
        y = temp
        # x,y = y,x # Another method
        print("x =", x, "y =", y)

    # else, we add up x and y in x, and we multiply x and y in y
    else:
        x += y
        y = x * y
        print("x =", x, "y =", y)

except ValueError:
    print("Please insert a numerical value in x and y")
