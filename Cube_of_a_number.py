def cube(n):
    return n ** 3

n = input("Number: ")

try:
    n = int(n)

    print(f"Cube of {n} is: ", cube(n))

except ValueError:
    print("Invalid input! ")




