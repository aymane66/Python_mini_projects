def get_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(int(input(f"Number {i + 1}: ")))
    return numbers


def get_largest_numbers(numbers, m):
    numbers.sort(reverse=True)
    largest_numbers = numbers[:m]
    return largest_numbers


n = int(input("Total elements of the list: "))
numbers = get_numbers(n)
print("Your list: ", numbers)

m = int(input("Number of largest numbers to display: "))
print(f"The {m} biggest numbers in your list are: ", get_largest_numbers(numbers, m))
