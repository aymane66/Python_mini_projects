print("------------- Calculator: Menu -------------")
op = 0
while True:
    try:

        print()
        print("1 - Addition")
        print("2 - Subtraction")
        print("3 - Multiplication")
        print("4 - Division")
        print("5 - Division remainder")
        print("6 - Power")
        print("-----------------------------")

        op = int(input("Operation: "))
        if op < 1 or op > 6:
            print("Invalid operator! Please insert choice between 1 to 6.")
        else:
            a = int(input("Number 1: "))
            b = int(input("Number 2: "))

            if op == 1:
                print(f"{a} + {b} = {a + b}")
            elif op == 2:
                print(f"{a} - {b} = {a - b}")
            elif op == 3:
                print(f"{a} x {b} = {a * b}")
            elif op == 4:
                if b != 0:
                    print(f"{a} / {b} = {a / b}")
                else:
                    print("Division by zero is not possible! ")
            elif op == 5:
                print(f"{a} % {b} = {a % b}")
            elif op == 6:
                print(f"{a} raised to the power of {b} = {a ** b}")

            again = input("Do you want to make another calculation? (Y/N) ")
            if again.lower() == "n":
                break
            elif again.lower() == "y":
                continue
            else:
                print("Invalid input! ")
                break
    except ValueError:
        print("Invalid input. Please insert numbers for calculation.")
