r = input("Rows: ")
c = input("Columns: ")

try:
    r = int(r)
    c = int(c)

    for i in range(1, r + 1):
        for j in range(1, c + 1):
            print(i, end=" ")
        print()

except ValueError:
    print("Invalid input! ")