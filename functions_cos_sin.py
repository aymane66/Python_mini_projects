from math import cos, sin, pi

def p1(x):
    s = 0
    for i in range(11):
        s += cos(i * x)
    return s


def p2(x):
    r = (1 / 2) + ((sin(((2 * 10 + 1) / 2) * x)) / (2 * sin(x / 2)))
    return r


x = input("Value of x: ")

try:
    x = int(x)

    print(format(p1(x), ".2f"))
    print(format(p2(x), ".2f"))

except ValueError:
    print("Invalid input! ")
