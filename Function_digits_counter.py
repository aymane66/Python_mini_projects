def digit_counter(n):
    count = 0

    while n != 0:
        n //= 10
        count += 1
    print(f"Number {m} has {count} digits. ")


n = input("Number: ")

try:
    n = int(n)
    m = n

    digit_counter(n)

except ValueError:
    print("Invalid input!")