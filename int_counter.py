# This program displays the number of digits in the inserted number.

n = int(input("Number: "))
r = n
count = 0

while n != 0:
    n = n // 10
    count += 1
print(f"Number of digits in {r} are: {count}")