def sign(a, b):
    if (a < 0 and b < 0) or (a > 0 and b > 0):
        print(f"Number {a} and {b} have the same sign. ")
    else:
        print(f"Number {a} and {b} do NOT have the same sign. ")


def max_num(a, b):
    if a > b:
        return a
    elif b > a:
        return b


def min_num(a, b):
    if a < b:
        return a
    elif b < a:
        return b


a = input("First number: ")
b = input("Second number: ")

try:
    a = int(a)
    b = int(b)

    sign(a, b)
    print("Max number:", max_num(a, b))
    print("Min number: ", min_num(a, b))

except ValueError:
    print("Invalid input! ")
