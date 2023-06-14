from math import cos, sin, pi


def func_1(x):
    return cos(4 * x)


def func_2(x):
    return -4 * sin(4 * x)


def func_3(x):
    return -16 * cos(4 * x)


print("f(0) ")
print("=", func_1(0))
print("=", func_2(0))
print("=", func_3(0))
print()

print("f(pi/2) ")
print("=", func_1(pi / 2))
print("=", format(func_2(pi / 2), ".2f"))
print("=", func_3(pi / 2))
print()

print("f(pi)")
print("=", func_1(pi))
print("=", format(func_2(pi), ".2f"))
print("=", func_3(pi))
print()

print("f(-(pi / 2))")
print("=", func_1(- (pi / 2)))
print("=", format(func_2(- (pi / 2)), ".2f"))
print("=", func_3(- (pi / 2)))
