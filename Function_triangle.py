def triangle(n):
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print("  ", end=" ")
        for j in range(1, 2 * i):
            print("* ", end=" ")

        print()


n = input("Number: ")

try:
    n = int(n)

    triangle(n)

except ValueError:
    print("Invalid input! ")