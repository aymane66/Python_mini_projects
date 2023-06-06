n = input("Number: ")
u = 6

try:
    n = int(n)

    for i in range(n):
        u = 4 * u + 10
    print("Result: ", u)

except ValueError:
    print("Invalid input! ")