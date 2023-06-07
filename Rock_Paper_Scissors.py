import random

print("--------------- Rock Paper Scissors ---------------")
name = input("What is your name? >>  ")

win = 0
draw = 0
lose = 0

while True:
    # Display available choices and get user input
    print("--------------- Choices  ---------------")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("--- Press q to quit the game ---")
    print()
    choice = input("Your turn: ")

    if choice == "q":
        break
    if choice not in ["1", "2", "3"]:
        print("Wrong input! Please choose 1, 2, or 3.")
        continue

    # Generate AI's choice
    ai = random.randint(1, 3)
    choice = int(choice)
    print(f"Computer: {ai}")

    # Compare choices and determine the winner
    if choice == ai:
        print("It's a draw! ")
        draw += 1
    elif (choice == 1 and ai == 3) or (choice == 2 and ai == 1) or (choice == 3 and ai == 2):
        print("You win! ")
        win += 1
    else:
        print("You lost! ")
        lose += 1


print("--------------- Score ---------------")
# Determine the winner based on the scores
if win > lose:
    print(f"Winner: {name}")
elif win < lose:
    print("Winner: Computer")
else:
    print("It's a draw!")

# Print the final scores
print(f"You won: {win} times")
print(f"You lost: {lose} times")
print(f"A draw: {draw} times")
print("--------------------------------------")
