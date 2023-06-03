year = input("Year: ")

try:
    year = int(year)

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(year, "is a leap year. ")
    else:
        print(year, "is NOT a leap year.")

except ValueError:
    print("Wrong input. ")