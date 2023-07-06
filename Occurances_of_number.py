numbers = []

for row in range(3):
    rows = []
    for col in range(4):
        rows.append(int(input(f"Insert number {row + 1} : ")))
    numbers.append(rows)

print("Matrix inserted: ")
for i in numbers:
    print(i)

x = int(input("Insert a number: "))
count = 0
for number in numbers:
    count = count + number.count(x)

print(f"Number {x} was mentioned {count} times.")
