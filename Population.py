# Population of two cities
marrakech = 1000000
agadir = 500000

years = 0
while marrakech > agadir:
    # Population growth every year
    agadir *= 1.08
    marrakech += 50000
    years += 1
print("Years for Agadir to surpass Marrakech: ", years, "years.")
