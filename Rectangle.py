r = input("Rows: ")
c = input("Columns: ")

try:
    r = int(r)
    c = int(c)

    for i in range(r):
        for j in range(c):
            print("* ", end=" ")
        print()

except ValueError:
    print("Invalid input. Please insert numbers for rows and columns. ")
