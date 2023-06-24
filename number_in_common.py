numbers_1 = []
numbers_2 = []

print("Insert 5 numbers for list 1: ")
for i in range(5):
    numbers_1.append(int(input(f"Number {i + 1}: ")))

print("Insert 5 numbers for list 2: ")
for i in range(5):
    numbers_2.append(int(input(f"Number {i + 1}: ")))

print("List 1: ", numbers_1)
print("List 2: ", numbers_2)

count = 0
for i in range(len(numbers_1)):
    if numbers_1[i] == numbers_2[i]:
        count += 1
print(f"List 1 and 2 have {count} numbers in common. ")