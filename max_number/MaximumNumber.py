from utils import find_max

numbers = []
while True:
    number = input("Insert  a number (insert 'done' to finish): ")
    if number == "done":
        break
    numbers.append(number)


max_num = find_max(numbers)
print(max_num)
