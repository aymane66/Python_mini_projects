
try:
    s = 0
    for i in range(1, 9):
        n = int(input(f"Number {i}: "))
        if n < 0:
            break
        s += n

    print("Total: ", s)

except ValueError:
    print("Invalid input! ")
