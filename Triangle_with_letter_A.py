n = input("Number: ")
A = chr(65)

try:
    n = int(n)

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(A, end=" ")
        print()

except ValueError:
    print("Invalid input! ")