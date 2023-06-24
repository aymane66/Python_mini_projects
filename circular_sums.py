# The purpose of this exercise is to not use the method .sort
numbers = []

for i in range(10):
    numbers.append(int(input(f"Number {i + 1}: ")))
print("Numbers inserted: ", numbers)

negative_numbers = []
positive_numbers = []

for number in numbers:
    if number < 0:
        negative_numbers.append(number)
    else:
        positive_numbers.append(number)

updated_numbers = negative_numbers + positive_numbers
print(updated_numbers)
