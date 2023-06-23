numbers = []

for i in range(10):
    num = int(input(f"Number {i + 1}: "))
    numbers.append(num)
print("Inserted numbers: ", numbers)

n = input("Number: ")
try:
    n = int(n)

    count = numbers.count(n)
    print(f"Number of occurrence of {n}: ", count)

except ValueError:
    print("Invalid input! ")
