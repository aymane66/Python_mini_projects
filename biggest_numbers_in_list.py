n = int(input("total elements of the list: "))

numbers = []

for i in range(n):
    numbers.append(int(input(f"Number {i + 1}: ")))

print("Your list: ", numbers)

m = int(input("Biggest numbers to display: "))

numbers.sort(reverse=True)
numbers_1 = [numbers[:m]]

print(f"The {m} biggest numbers in your list are: ", numbers_1)
