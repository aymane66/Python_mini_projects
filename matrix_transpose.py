print("Insert the number of columns and rows: ")
columns = int(input("Columns: "))
rows = int(input("Rows: "))


matrix = [[int(input("Number: ")) for i in range(columns)] for j in range(rows)]

print("Inserted matrix: ")
for m in matrix:
    print(m)

transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print("Transposed matrix: ")
for t in transposed:
    print(t)
