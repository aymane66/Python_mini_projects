numbers = []

for i in range(10):
    num = int(input(f"Number {i + 1}: "))
    numbers.append(num)
print(numbers)

print("Biggest number: ", max(numbers))
print("Smallest number: ", min(numbers))