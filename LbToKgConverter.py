weight = input("Please enter your weight: ")
unit = input("Select the unit of measurement (K = kg, L = lbs): ")

try:
    weight = float(weight)

    if unit.lower() == "k":
        r = weight * 2.205
        print("Your weight in pounds is: ", format(r, ".2f"), "lbs")

    elif unit.lower() == "l":
        r = weight / 2.205
        print("Your weight in kilograms is: ", format(r, ".2f"), "kg")
    else:
        print("Error: Invalid unit of measurement. Please select either 'K' or 'L'.")

except ValueError:
    print("Invalid input. Please enter a number for weight.")
