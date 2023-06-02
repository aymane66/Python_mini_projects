name = input("Insert your name: ")

if len(name) < 3:
    print("Name must be at least 3 characters. ")
elif len(name) > 50:
    print("Name can be 50 characters max. ")
else:
    print("You are good to go. ")