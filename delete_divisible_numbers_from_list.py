def get_numbers(numbers):
    n = int(input("Numbers in list: "))
    for i in range(n):
        numbers.append(int(input(f"Number {i + 1}: ")))
    return numbers


def delete_divisors(numbers):
    updated_numbers = []
    for i in numbers:
        if i % 5 != 0:
            updated_numbers.append(i)
    return updated_numbers


numbers = []
print("List inserted: ", get_numbers(numbers))
print("List after removing divisors of 5: ", delete_divisors(numbers))
