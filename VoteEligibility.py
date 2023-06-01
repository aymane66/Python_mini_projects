age = input("Insert your age: ")

try:
    age = int(age)

    msg = "You are eligible to vote." if age >= 18 else "You are NOT eligible to vote."
    print(msg)

except ValueError:
    print("Error. Please insert a number.")
