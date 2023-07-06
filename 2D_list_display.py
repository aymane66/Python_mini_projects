list = [["html", "css", "javascript"] , ["bash", "c"], ["python", "sql"]]

# Method 1:
for i in list:
    for j in i:
        print(j, end=" ")
    print()

print()

# Method 2:
for i in range(len(list)):
    for j in range(len(list[i])):
        print(list[i][j], end=" ")
    print()
print()

# Method 3:
for row in list:
    print(row)