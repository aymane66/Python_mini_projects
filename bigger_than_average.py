numbers = []
for i in range(10):
    num = float(input(f"Score {i + 1}: "))
    numbers.append(num)
print("Scores: ", numbers)

average_score = sum(numbers) / len(numbers)
print("Average score: ", average_score)

above_av = []
for i in numbers:
    if i > average_score:
        above_av.append(i)
print("Scores above average: ", above_av)
