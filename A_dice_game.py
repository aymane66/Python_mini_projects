from random import randint

win_counter = 0

for i in range(100001):
    x = randint(1, 6)
    if x == 2 or x == 5:
        win_counter += 1

print("----------------------- Dice toss simulator -----------------------------")
print(f"You won {win_counter} times out of 100000 tosses. ")