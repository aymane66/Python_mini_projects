# This program counts the sum of numbers 1/2 + 1/2 ... + 1/n

n = input("Number: ")

try:
    n = int(n)
    s = 0

    for i in range(1, n + 1):
        s += 1 / i
    print("Total: ", format(s, ".2f"))

except ValueError:
    print("Invalid input! ")