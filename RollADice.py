import random


class Dice:
    def roll_dice(self):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        roll = (a, b)
        print(roll)


dice = Dice()
print("Roll a dice: ")
dice.roll_dice()

