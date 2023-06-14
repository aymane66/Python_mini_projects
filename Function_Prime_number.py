def is_prime(n):
    count = 1
    for i in range(2, n // 2):
        if n % 2 == 0:
            count = 0
            break
    if count == 1:
        print(f"Number {n} is a prime number. ")
    else:
        print(f"Number {n} is NOT a prime number. ")


n = input("Number: ")

try:
    n = int(n)

    is_prime(n)

except ValueError:
    print("Invalid input! ")
