import math

xa = int(input("Insert Xa: "))
xb = int(input("Insert Xb: "))

ya = int(input("Insert Ya: "))
yb = int(input("Insert Yb: "))

ab = math.sqrt(pow((xb - xa), 2) + pow((yb - ya), 2))
print("Distance between A and B is: ", format(ab, ".2f"))
