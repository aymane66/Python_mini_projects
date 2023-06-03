character = input("Insert a character: ")

if "a" <= character.lower() <= "z":
    print(character, "is an alphabet. ")
elif "0" <= character <= "9":
    print(character, "is a number. ")
else:
    print(character, "is a special character. ")