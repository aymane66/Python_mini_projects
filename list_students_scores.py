algebra = [10, 12, 14.5, 6, 2.5]
statistics = [13, 15, 18, 10.5, 7]
geometry = [16.5, 13.75, 15, 13, 12.25]
arts = [18, 14, 17.25, 16, 15.5]

all_scores = algebra + statistics + geometry + arts
total = sum(all_scores)
average = total / len(all_scores)
print("Total: ", total)
print("Average: ", format(average, ".2f"))
print("Highest score: ", max(all_scores))
print("Lowest score: ", min(all_scores))
