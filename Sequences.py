n = input("Number: ")
u = 6

try:
    n = int(n)

    for i in range(n):
        u = 4 * u + 10
    print(f"U {i + 1} = ", u)

except ValueError:
    print("Invalid input! ")