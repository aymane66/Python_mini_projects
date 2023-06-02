temp = input("Temperature in C°: ")

try:
    temp = float(temp)
    if temp > 30:
        print("It´s a hot day!")
    elif temp < 10:
        print ("It´s a cold day!")
    else:
        print ("It´s a cool day!")
except ValueError:
    print("Invalid input. Please insert a number. ")