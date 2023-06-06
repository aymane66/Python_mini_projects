n = 0
while n < 2:
    n = int(input("Number: "))
upp = 0
up = 1

print("------ Result ------")
print(upp, up, end=" ")

for i in range(n - 1):
    u = upp + up
    print(u, end=" ")
    upp = up
    up = u
