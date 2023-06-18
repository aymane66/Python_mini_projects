import math
n = input("Number: ")

try:
    n = int(n)

    m = math.factorial(n)
    print(f"Factorial of {n} is {m}")

except ValueError:
    print("Invalid input! ")