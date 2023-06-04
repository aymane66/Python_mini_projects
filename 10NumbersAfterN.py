n = input("Number: ")

try:
    n = int(n)

    for i in range(n, n + 10):
        print(i + 1, end=" ")

except ValueError:
    print("Error. Please insert a number.")