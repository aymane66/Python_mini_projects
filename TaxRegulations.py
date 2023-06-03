age = input("Insert your age: ")
gender = input("Insert your gender (F- Female M - Male): ")

try:
    age = int(age)

    if gender.lower() == "m" and age > 20:
        print("You are eligible to pay taxes")
    elif gender.lower() == "f" and 18 <= age <= 35:
        print("You are eligible to pay taxes")
    else:
        print("You are not eligible to pay taxes.")

except ValueError:
    print("Invalid input.")