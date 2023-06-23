word = input("Insert a word: ")
word_list = list(word)

word_list1 = word_list[::-1]

if word_list1 == word_list:
    print(f"The word {word} is palindrome. ")
else:
    print(f"The word {word} is NOT palindrome. ")
