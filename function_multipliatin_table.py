def multiply(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

while True:
    n = input("Number: ")

    try:
        n = int(n)

        if n > 0:
            multiply(n)
            break
        else:
            print("Only insert a positive number. ")


    except ValueError:
        print("Invalid input! ")