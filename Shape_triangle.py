n = input("Number: ")

try:
    n = int(n)

    for i in range(1, n + 1):
        for j in range(i):
            print("* ", end=" ")
        print("")

except ValueError:
    print("Invalid input! ")