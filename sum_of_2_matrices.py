print("Insert the number of rows and columns for both matrices: ")
rows = int(input("Rows: "))
columns = int(input("Columns: "))

print("Let´s fill in matrix 1: ")
matrix_1 = [[int(input("Number: ")) for i in range(columns)] for j in range(rows)]

print("Let´s fill in matrix 2: ")
matrix_2 = [[int(input("Number: ")) for m in range(columns)] for n in range(rows)]

print()
print("Matrix 1: ")
print()
for i in matrix_1:
    print(i)

print()
print("Matrix 2: ")
print()
for i in matrix_2:
    print(i)

result = [[0 for i in range(columns)] for j in range(rows)]

for i in range(len(matrix_1)):
    for j in range(len(matrix_1[0])):
        result[i][j] = matrix_1[i][j] + matrix_2[i][j]

print()
print("Sum of matrix 1 and matrix 2: ")
print()
for r in result:
    print(r)
