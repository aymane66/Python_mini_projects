print("----- Insert your scores out of 20 -----")
n1 = input("Score 1: ")
n2 = input("Score 2: ")
n3 = input("Score 3: ")

try:
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)

    average = (n1 + n2 + n3) / 3
    if (average >= 0) and (average <= 20):
        print("Score: ", format(average, ".2f"), "/20")
    else:
        print("Invalid score!")

    if average < 10:
        print("Fail!")
    elif average == 10:
        print("Pass!")
    elif average < 14:
        print("Good!")
    elif average < 17:
        print("Very good!")
    elif average < 19:
        print("Excellent!")
    elif average == 20:
        print("Outstanding!")
    else:
        print("Invalid input")

except ValueError:
    print("Error. Please insert a number for scores. ")
