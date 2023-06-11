n = input("Number: ")

try:
    n = int(n)

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            c = chr(64 + j)
            print(c, end=" ")
        print()

except ValueError:
    print("Invalid input! ")
