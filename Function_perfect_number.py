def perfect_num(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if n == s:
        print(n)


print("Perfect numbers between 1 and 10000 are: ")
for i in range(1, 10000):
    perfect_num(i)
