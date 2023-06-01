hours = int(input("Enter Hours: "))
rate = float(input("Enter rate: "))

if hours > 40:
    overtime = hours - 40
    pay = (hours * rate) + (overtime * (rate * 0.5))
else:
    pay = hours * rate

print("Pay: ", format(pay, ".2f"))
