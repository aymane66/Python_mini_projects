# Study while loops first
n = input("Number: ")

try:
    n = int(n)
    i = 1
    while i <= 10:
        print(n + i, end=" ")
        i += 1

except ValueError:
    print("Error. Please insert a number. ")