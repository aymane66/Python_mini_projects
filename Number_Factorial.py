print("---------- Factorial Calculator ----------")

while True:
    n = (input("Number: "))

    try:
        n = int(n)

        if n >= 0:
            r = 1

            if n == 0:
                print("Result: 1")

            else:
                for i in range(1, n + 1):
                    r = r * i
                print("Result: ", r)

    except ValueError:
        print("Invalid input. Insert a number. ")
