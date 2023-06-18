def syracuse(n):
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        print(n)


n = input("Number: ")

try:
    n = int(n)
    print(n)
    syracuse(n)

except ValueError:
    print("invalid input! ")