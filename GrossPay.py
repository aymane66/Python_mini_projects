hours = input("Enter Hours: ")
rate = input("Enter rate: ")

try:
    ho = float(hours)
    r = float(rate)

except:
    print("Error, please enter numeric input. ")
    quit()

if ho > 40:
    overtime = ho - 40
    pay = (ho * r) + (overtime * (r * 0.5))
else:
    pay = ho * r

print("Pay: ", format(pay, ".2f"))
