numbers = []
count = int(input("How many numbers do you want to insert? "))

for i in range(count):
    num = int(input(f"Number {i + 1}: "))
    numbers.append(num)
print("Numbers entered:", numbers)

total = sum(numbers)
average = total / len(numbers)
print("Total:", total)
print("Average: {:.2f}".format(average))

print("Product: ")


# Complete after finishing the course