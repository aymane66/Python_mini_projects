n = input("Number: ")

try:
    n = int(n)

    for i in range(1, n + 1):
        for j in range(1, 6):
            if (j == 1 or j == 5) and (i != 1):
                print("* ", end="")
            elif (i == 1 or i == (n + 1) // 2) and (j > 1 and j < 5):
                print("* ", end="")
            else:
                print("  ", end="")
        print()

except ValueError:
    print("Invalid input! ")
