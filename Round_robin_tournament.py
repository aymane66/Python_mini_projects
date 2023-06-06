teams = int(input("Number of teams: "))

for i in range(1, teams + 1):
    for j in range(1, teams + 1):
        if i != j:
            print(f"Team {i} vs Team {j}")
