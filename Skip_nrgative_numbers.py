try:
    s = 0
    for i in range(1, 9):
        n = int(input(f"Number {i}: "))

        if n < 1:
            continue
        s += n
    print("Result: ", s)

except ValueError:
    print("Invalid input! ")
