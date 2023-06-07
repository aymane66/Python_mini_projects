n = input("Number: ")

try:
    n = int(n)
    r = n
    rev = 0
    while n != 0:
        rev = (rev * 10) + (n % 10)
        n = n // 10
    if r == rev:
        print(f"Number {r} is palindrome.")
    else:
        print(f"Number {r} is NOT palindrome. ")

except ValueError:
    print("Invalid input! Please insert a number. ")
