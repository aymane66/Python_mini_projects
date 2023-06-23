numbers = []

for i in range(10):
    num = int(input(f"Number {i + 1}: "))
    numbers.append(num)
print("Numbers inserted: ", numbers)

search = int(input("Look for: "))

if search in numbers:
    print(f"Number {search} is found in the list. ")
else:
    print(f"Number {search} is NOT found in the list. ")