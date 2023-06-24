text = list(input("Insert a sentence: "))
letter = input("Count occurrences of letter: ")

#Method 1:
#count = text.count(letter)

#Method 2:
count = 0
for char in text:
    if letter.lower() == char.lower():
        count +=1
print(f"Result: Letter ({letter}) was mentioned in the text {count} times.")