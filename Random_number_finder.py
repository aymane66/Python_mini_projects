import random
print("Hey! I chose a number between 1 and 30. Can you guess it? ")
print("You have 5 trials!")
print("-----------------------------")
n = random.randint(1, 30)
t = 0

while t < 6:
    g = int(input("Guess the number: "))
    t += 1

    if g == n:
        print(f"Correct! You found {n} in {t} trials. ")
        break
    elif g < n:
        print("Hint: It´s a bigger number. ")

    else:
        print("Hint: It´s a smaller number. ")
else:
    print("I am sorry. You lost the game. The secret number was", n)
