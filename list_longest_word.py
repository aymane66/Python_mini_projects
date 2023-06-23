languages = ["Html", "Css", "Bash", "C", "Python", "JavaScript"]
print(languages)
languages.sort(key=len, reverse=True)

print("Longest word in the list: ",languages[0])
