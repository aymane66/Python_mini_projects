# This program removes duplicates from the list
numbers = [1, 2, 2, 3, 4, 3, 4, 5, 6, 7, 7, 8, 9, 1]

new_numbers = []

for i in numbers:
    if i not in new_numbers:
        new_numbers.append(i)
print(new_numbers)
