u = []
for i in range(3):
    x = int(input(f"Insert value {i + 1}: "))
    u.append(x)
print("Vector A: ", u)

v = []
for i in range(3):
    x = int(input(f"Insert value {i + 1}: "))
    v.append(x)
print("Vector B: ", v)

print("------ Scalar product of vector A & B: ------ ")

product = u[0] * v[0] + u[1] * v[1] + u[2] * v[2]
print("Result: ", product)
