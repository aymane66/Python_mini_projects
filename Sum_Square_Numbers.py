import math

print("---------- Sum of Square Numbers Calculator ----------")
n = input("Number: ")

try:
    n = int(n)
    s = 0
    j = 1

    for i in range(n):
        s += math.pow(j, 2)
        j += 2
    print("Result: ", s)

except ValueError:
    print("Invalid input! ")