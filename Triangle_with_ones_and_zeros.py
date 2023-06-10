n = input("Number: ")

try:
    n = int(n)

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            n = j % 2
            print(n, end=" ")
        print()

except ValueError:
    print("Invalid input! ")