n = input("Number: ")

try:
    n = int(n)

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    for i in range(1, n):
        for j in range(n - 1, i - 1, - 1):
            print(n - j, end=" ")
        print()

except ValueError:
    print("Invalid input! ")
