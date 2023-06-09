n = input("Number: ")

try:
    n = int(n)
    p = 1
    for i in range(1, n * 2 - 1 + 1):
        for j in range(1, p + 1):
            print("* ", end="")
        if i < n:
            p += 1
        else:
            p -= 1
        print()


except ValueError:
    print("Invalid input! ")