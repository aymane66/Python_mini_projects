numbers = input("Insert numbers in digits (0 to 9): ")

dictionary = {
    "0": "Zero ",
    "1": "One ",
    "2": "Two ",
    "3": "Three ",
    "4": "Four ",
    "5": "Five ",
    "6": "Six ",
    "7": "Seven ",
    "8": "Eight ",
    "9": "Nine ",
    }

for i in numbers:
    print(dictionary[i], end="")

