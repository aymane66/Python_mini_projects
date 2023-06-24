programming_languages = ['Python', 'JavaScript', 'Java', 'C++', 'C#', 'Ruby', 'Go', 'Swift', 'Rust', 'PHP']
creators = ['Guido van Rossum', 'Brendan Eich', 'James Gosling', 'Bjarne Stroustrup', 'Anders Hejlsberg', 'Yukihiro Matsumoto', 'Robert Griesemer, Rob Pike, and Ken Thompson', 'Chris Lattner', 'Graydon Hoare', 'Rasmus Lerdorf']
creation_dates = [1991, 1995, 1995, 1983, 2000, 1995, 2009, 2014, 2010, 1994]

print("---- Info about Programming languages ----")

number = 0
for language, creator, date in zip(programming_languages, creators, creation_dates):
    number += 1
    print(f"{number}- {language} was created by {creator} in {date}. ")