while True:
    try:
        n = int(input("Number: "))

        if n > 1:
            s = 0
            for i in range(n + 1):
                s += i
            print("Total: ", s)
            break
        else:
            print("Invalid input. Please insert a number bigger than 1. ")

    except ValueError:
        print("Error. Please insert an integer. ")
