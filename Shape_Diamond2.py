n = input("Number: ")

try:
    n = int(n)
    st = 1
    space = n - 1

    for i in range(1, n * 2):
        for j in range(0, space):
            print("  ", end="")
        for j in range(1, st * 2):
            print("* ", end="")

        if i < n:
            space -= 1
            st += 1
        else:
            space += 1
            st -= 1
        print()


except ValueError:
    print("Invalid input!")
