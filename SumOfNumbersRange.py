n = input("Insert a number: ")

try:
    n = int(n)

    total = 0
    for i in range(n+1):
        total += + i
    print(f"Sum of numbers form 1 to {n} is:", total)

except ValueError:
    print("Invalid input! ")

