n = input("Number: ")
m = n
try:
    n = int(n)
    b = 0
    order = 0
    while n != 0:
        r = n % 2
        p = 10 ** order
        b += r * p
        order += 1
        n = n // 2
    print(f"Number {m} in binary system is: {b}", end=" ")

except ValueError:
    print("Invalid input! ")
