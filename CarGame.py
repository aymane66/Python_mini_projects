command = ""

while True:
    command = input("Command -> ").lower()
    if command == "help":
        print("""
    start - to start the car
    stop - to stop the car
    quit - to exit
        """)
    elif command == "start":
        print("Car started ... Ready to go!")
        if command == "start":
            print("The car has already started ..")
    elif command == "stop":
        print("Car stopped!")
        if command == "stop":
            print("The car has already stopped ..")
    elif command == "quit":
        quit()
    else:
        print("Error. Wrong command")

