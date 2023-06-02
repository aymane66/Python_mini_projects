r1 = input("Enter the resistance value for R1: ")
r2 = input("Enter the resistance value for R2: ")
r3 = input("Enter the resistance value for R3: ")

try:
    r1 = float(r1)
    r2 = float(r2)
    r3 = float(r3)

    r_ser = r1 + r2 + r3
    r_par = (r1 * r2 * r3) / (r1 * r2 + r1 * r3 + r2 * r3)

    print("----- Result: -----")
    print("Series: ", format(r_ser, ".2f"))
    print("Parallel: ", format(r_par, ".2f"))

except ValueError:
    print("Error. Please insert a valid integer for the resistance value.")