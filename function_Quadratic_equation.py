import math


def solutions(a, b, c):
    delta = math.pow(b, 2) - 4 * a * c
    if delta > 0:
        print("This equation has two solutions: ")
        s1 = (-b - math.sqrt(delta)) / (2 * a)
        print("Solution 1: ", format(s1, ".2f"))
        s2 = (-b + math.sqrt(delta)) / (2 * a)
        print("Solution 2:", format(s2, ".2f"))
    elif delta == 0:
        x = (-b) / (2 * a)
        print(f"This equation has one solution: ", format(x, ".2f"))
    else:
        print("This equation has no solution in R ")


a = input("Value of a: ")
b = input("Value of b: ")
c = input("Value of c: ")

try:
    a = int(a)
    b = int(b)
    c = int(c)

    solutions(a, b, c)

except ValueError:
    print("Invalid input! ")
