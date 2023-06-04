message = input("How do you feel today? (happy/sad) >> ")
words = message.split(" ")

emojis = {
    "happy": ":)",
    "sad": ":(",
}

output = ""
for i in words:
    output += emojis.get(i, i) + " "
print(output)
