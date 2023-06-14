def leap_year(year):
    if ((year % 100 != 0) and (year % 4 == 0) or (year % 400 == 0)):
        print(f"Year {year} is a leap year. ")
    else:
        print(f"Year {year} is NOT a leap year. ")


year = input("Year: ")

try:
    year = int(year)
    leap_year(year)

except ValueError:
    print("Invalid input! ")