n = input("Number: ")

try:
    n = int(n)

    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print("  ", end="")
        for j in range(1, 2 * i - 1 + 1):
            if j == 1 or j == 2 * i - 1 or i == n:
                print("* ", end="")
            else:
                print("  ", end="")
        print()

except ValueError:
    print("Invalid input! ")