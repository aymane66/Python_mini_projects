n = int(input("Number: "))
isprime = 1
for i in range(2, int(n / 2) + 1):
    if n % i == 0:
        isprime = 0
        break
if isprime == 1:
    print(f"{n} is a prime number. ")
else:
    print(f"{n} is NOT a prime number. ")