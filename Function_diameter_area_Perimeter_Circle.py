import math


def diameter():
    return radius * 2


def perimeter():
    return 2 * math.pi * radius


def surface():
    return math.pi * pow(radius, 2)


radius = input("Circle radius: ")

try:
    radius = float(radius)

    print("--------------- Circle info: ---------------")
    print("Diameter: ", format(diameter(), ".2f"))
    print("Perimeter: ", format(perimeter(), ".2f"))
    print("Surface: ", format(surface(), ".2f"))
    print("--------------------------------------------")


except ValueError:
    print("Invalid input! ")
