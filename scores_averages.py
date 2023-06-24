names = []
scores_1 = []
scores_2 = []

for i in range(5):
    name = input(f"Student´s name {i + 1}: ")
    names.append(name)
    s1 = int(input("Score of first exam: "))
    scores_1.append(s1)
    s2 = int(input("Score of second exam: "))
    scores_2.append(s2)

averages = []
for i in range(len(scores_1)):
    average = (scores_1[i] + scores_2[i]) / 2
    averages.append(average)

for name, average in zip(names, averages):
    print(f"Student´s name: {name}\nStudent´s average score: {average}\n")
