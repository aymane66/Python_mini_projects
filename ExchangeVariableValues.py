x = int(input("Insert value of x: "))
y = int(input("Insert value of y: "))

# ----- Method 1 -----
#tmp = x
#x = y
#y = tmp

# ----- Method 2 -----
x, y = y, x

print("----- Value exchanged -----")
print("Value of x: ", x)
print("Value of y: ", y)
