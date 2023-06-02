secret_number = 9
count = 0
limit = 3

while count < limit:
    guess = int(input("Guess: "))
    count += 1
    if guess == secret_number:
        print("You win! ")
        break
else:
    print("You lost! ")
