n = input("Number: ")

try:
    n = int(n)
    count = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            count += 1
            c = chr(64 + count)
            print(c, end=" ")
        print()

except ValueError:
    print("Invalid input! ")