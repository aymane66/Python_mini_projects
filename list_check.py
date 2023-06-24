x = input("Search for number: ")

try:
    x = int(x)

    numbers = []
    for i in range(5):
        num = input(f"Insert number {i + 1}: ")
        try:
            num = int(num)

            numbers.append(num)
        except ValueError:
            print("Invalid input! ")

    print("List of numbers inserted: ", numbers)

    if x in numbers:
        print(f"Number {x} is in the list. ")
    else:
        print(f"Number {x} is NOT in the list. ")

except ValueError:
    print("Invalid input! ")