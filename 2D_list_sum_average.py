scores = []
for subject in range(4):
    rows = []
    for student in range(5):
        rows.append(float(input(f"Insert score {subject + 1} of student {student + 1}: ")))
    scores.append(rows)

print("Scores: ")
for i in scores:
    for j in i:
        print(j, end="  ")
    print()

total = 0
for i in scores:
    total += sum(i)
print("Total: ", total)

average = total / (len(scores) * len(scores[0]))
print("Average: ", average)