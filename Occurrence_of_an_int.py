numbers = []

for i in range(10):
    num = int(input(f"Number {i + 1}: "))
    numbers.append(num)
print("Inserted numbers: ", numbers)

search = input("Number: ")
try:
    search = int(search)

    count = numbers.count(search)
    print(f"Number of occurrence of number {search}: ", count)

except ValueError:
    print("Invalid input! ")
