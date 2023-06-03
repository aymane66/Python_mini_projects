command = input("Command: ")

try:
    command = int(command)

    if command == 6:
        print("The character goes right. ")
    elif command == 4:
        print("The character goes left. ")
    elif command == 8:
        print("The character goes up. ")
    elif command == 2:
        print("The character goes down. ")
    else:
        print("Wrong command. The character does not move.")

except ValueError:
    print("Invalid input. ")