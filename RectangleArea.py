print("Let´s calculate the area and perimeter of a rectangle")
width = float(input("Insert the width of the rectangle: "))
length = float(input("Insert the length of the rectangle: "))

area = width * length
perimeter = 2 * (length + width)

print("----- Result -----")
print("Area of the rectangle: ", format(area, ".2f"))
print("Perimeter of the rectangle: ", format(perimeter, ".2f"))