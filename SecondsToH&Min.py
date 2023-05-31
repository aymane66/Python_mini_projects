n = int(input("Insert number of seconds: "))

hou = n // 3600
min = (n % 3600) // 60
sec = n % 60

print("----- Result -----")
print(hou, "hours", min, "minutes", sec, "seconds")
