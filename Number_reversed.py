n = int(input("Number: "))
m = n
inv = 0

while n != 0:
    inv = (inv * 10) + (n % 10)
    n = n // 10
print(f"The number {m}  reversed is: {inv}")
