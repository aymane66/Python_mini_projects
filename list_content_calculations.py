numbers = []
print("Insert 10 numbers: ")
for i in range(10):
    num = float(input(f"Number {i + 1}: "))
    numbers.append(num)

print(numbers)

print("Total: ", sum(numbers))
print("Average: ", sum(numbers) / len(numbers))

product = 1
for i in numbers:
    product *= i
print("Product: ", product)
