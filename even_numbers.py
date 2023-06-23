numbers = []
for i in range(10):
    num = int(input(f"Number {i + 1}: "))
    numbers.append(num)
print("Inserted numbers: ", numbers)

even_numbers = []
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
print("Even numbers: ", even_numbers)
