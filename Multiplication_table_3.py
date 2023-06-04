print("------ Multiplication table ------")

n = int(input("Number [1 - 10}: "))

while n < 1 or n > 10:
    n = int(input("Number: "))

i = 0
while i <= 10:
    r = n * i
    print(n, "x", i, "=", r)
    i += 1