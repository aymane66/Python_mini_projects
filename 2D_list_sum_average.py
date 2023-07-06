scores = []
for subject in range(2):
    rows = []
    for student in range(3):
        rows.append(float(input(f"Insert score {subject + 1} of student {student + 1}: ")))
    scores.append(rows)
print("Scores: ", scores)

total = 0
for i in scores:
    total += sum(i)
print("Total: ", total)

average = total / (len(scores) * len(scores[0]))
print("Average: ", average)