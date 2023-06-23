numbers = []
print("Insert 10 numbers: ")
for i in range(10):
    num = int(input(f"Number {i + 1}: "))
    numbers.append(num)

numbers_list = numbers.copy()
print(numbers_list)

print("Total: ", sum(numbers_list))
print("Average: ", sum(numbers_list) / len(numbers_list))

product = 1
for i in numbers_list:
    product *= i
print("Product: ", product)