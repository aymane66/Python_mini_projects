def perfect_num(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if n == s:
        print(f"Number {m} is a perfect number. ")
    else:
        print(f"Number {m} is NOT a perfect number. ")


n = input("Number: ")
m = n
try:
    n = int(n)

    perfect_num(n)

except ValueError:
    print("Invalid input! ")
