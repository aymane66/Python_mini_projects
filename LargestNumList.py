numbers = [16, 22, 54, 79, 48, 29, 86, 79, 80, 10]

max_number = numbers[0]

for i in numbers:
    if max_number < i:
        max_number = i

print("Largest number is: ", max_number)
