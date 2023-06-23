numbers = []

for i in range(10):
    num = int(input(f"Number {i + 1}: "))
    numbers.append(num)
print(numbers)

numbers.sort()
print("Second biggest number: ", numbers[-2])