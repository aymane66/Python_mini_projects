import math

n = input("Power of 10: ")

try:
    n = int(n)
    s = 0

    for i in range(0, n + 1):
        s += math.pow(10, i)
    print("Total: ", int(s))

except ValueError:
    print("Invalid input!")