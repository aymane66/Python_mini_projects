copies = input("Insert number of copies: ")

try:
    copies = int(copies)
    if copies <= 10:
        cost = copies * 0.30
        print("Cost: ", format(cost, ".2f"), "MAD")

    elif copies > 30:
        cost = 10 * 0.30 + 20 * 0.25 + (copies - 30) * 0.20
        print("Cost: ", format(cost, ".2f"), "MAD")

    else:
        cost = 10 * 0.30 + (copies - 10) * 0.25
        print("Cost: ", format(cost, ".2f"), "MAD")

except ValueError:
    print("Error. Please insert a numerical value. ")
