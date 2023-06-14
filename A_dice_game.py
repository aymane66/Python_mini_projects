from random import randint

print("----------------- Dice simulator game -----------------")
win_counter = 0

for i in range(1001):
    x = randint(1, 6)
    if x == 2 or x == 5:
        print("You win!! ")
        win_counter += 1
    else:
        print("You lost! ")

print("----------------------- Score -----------------------------")
print(f"You won {win_counter} times out of 1000 tosses. ")