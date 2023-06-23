numbers = []

for i in range(10):
    num = int(input(f"Number {i + 1}: "))
    numbers.append(num)
print("Numbers inserted: ", numbers)

numbers_1 = []
for i in numbers:
    if numbers.count(i) == 1:
        numbers_1.append(i)

print("Unique Numbers: ", numbers_1)

