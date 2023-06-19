import calendar

month = input("Month (1 to 12): ")
year = input("Year (1 to 9999): ")

try:
    month = int(month)
    year = int(year)

    if 1 <= month <= 12 and 1 <= year <= 9999:
        print(calendar.month(theyear=year, themonth=month))
    else:
        print("Invalid input! Please enter valid values for the month (1-12) and year (1-9999).")

except ValueError:
    print("Invalid input! Please enter valid integers for the month and year.")