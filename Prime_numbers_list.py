n = input("Insert a number: ")

try:
    n = int(n)
    prime_numbers = []
    x = 2

    while len(prime_numbers) < n:
        isprime = True

        for i in range(2, x):
            if x % i == 0:
                isprime = False
                break

        if isprime:
            prime_numbers.append(x)

        x += 1

    print(f"The {n} prime numbers are: {prime_numbers}")

except ValueError:
    print("Invalid input! ")
