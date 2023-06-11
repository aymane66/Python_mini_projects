n = input("Number: ")

try:
    n = int(n)
    char = 0
    count = 0
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print(" ", end=" ")
        for j in range(1, 2 * i):
            char = chr(11606 + count)
            print(char, end=" ")
            count += i
        print()


except ValueError:
    print("Invalid input! ")