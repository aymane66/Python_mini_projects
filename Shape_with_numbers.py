n = input("Number: ")

try:
    n = int(n)

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        for j in range(1, n * 2 - i * 2 + 1):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print(i - j + 1, end=" ")
        print()

except ValueError:
    print("Invalid input! ")