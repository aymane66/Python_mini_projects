import math

print("----- Quadratic Equation -----")
a = input("Value of A: ")
b = input("Value of B: ")
c = input("Value of C: ")

try:
    a = float(a)
    b = float(b)
    c = float(c)

    delta = b * b - 4 * a * c

    if delta < 0:
        print("This equation has no solution in R")
    elif delta == 0:
        solution = -b / (2 * a)
        print("Solution: ", solution)
    else:
        solution1 = (-b - math.sqrt(delta)) / (2 * a)
        print("Solution 1 : ", solution1)
        solution2 = (-b + math.sqrt(delta)) / (2 * a)
        print("Solution 2: ", solution2)

except ValueError:
    print("Invalid input. Insert a numeric number. ")