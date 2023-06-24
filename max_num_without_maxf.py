numbers = []

for i in range(5):
    num = int(input(f"Number {i + 1}: "))
    numbers.append(num)
print("Inserted numbers: ", numbers)

maximum = numbers[0]

for i in range(len(numbers)):
    if maximum < numbers[i]:
        maximum = numbers[i]
print("Max number: ", maximum)
