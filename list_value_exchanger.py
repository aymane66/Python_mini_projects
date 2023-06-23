countries = ["Norway", "Sweden", "Portugal", "Canada", "Finland"]
print(countries)

print("Let´s exchange the places of 2 countries: ")
option_1 = input("Choose your first option : ")
option_2 = input("Choose your second option: ")

op1 = countries.index(option_1)
op2 = countries.index(option_2)

countries[op1] , countries[op2] = countries[op2] , countries[op1]

print(countries)