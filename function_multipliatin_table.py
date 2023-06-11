def multiply(n):
    for i in range(1, 10 + 1):
        print(f"{n} x {i} = {n * i}")


n = input("Number: ")

try:
    n = int(n)

    if n > 0:
        multiply(n)
    else:
        print("Only insert a positive number. ")


except ValueError:
    print("Invalid input! ")