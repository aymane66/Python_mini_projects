a = input("Number 1: ")
b = input("Number 2: ")

try:
    a = int(a)
    b = int(b)

# checking for the smallest number. This is not necessary, but efficient
    if a > b:
        m = a
    else:
        m = b
    gcd = 0
    for i in range(1, m + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    print(f"Greatest common divisor of {a} and {b} is: {gcd}")

except ValueError:
    print("Invalid input! Please insert a number. ")
