age = input("Insert age: ")

try:
    age = int(age)

    if age < 0:
        print("Invalid number. ")
    elif age == 0:
        print("Newborn")
    elif age < 2:
        print("Infant")
    elif age <= 3:
        print("Toddler")
    elif age < 6:
        print("Preschool")
    elif age <= 12:
        print("Child")
    elif age <= 19:
        print("Teenager")
    else:
        print("Adult")

except ValueError:
    print("Invalid input. Please enter a number.")