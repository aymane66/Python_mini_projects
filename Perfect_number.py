n = input("Number: ")

try:
    n = int(n)
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += + i
    if n == s:
        print(f"Number {n} is a perfect number. ")
    else:
        print(f"Number {n} is NOT a perfect number. ")

except ValueError:
    print("Invalid input! ")