numbers = []

for i in range(6):
    numbers.append(int(input(f"Number {i + 1}: ")))
print("Numbers inserted: ", numbers)

numbers_rev = []
numbers_rev.extend(numbers[::-1])
print("Reversed: ", numbers_rev)
