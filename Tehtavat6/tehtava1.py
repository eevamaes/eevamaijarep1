import random
def noppa():
    return random.randint(1, 6)

silmaluku = noppa()
while silmaluku<6:
        print("Heitetään noppaa")
        silmaluku =noppa()
        print(silmaluku)
else:
    print("Saatiin kuutonen, nyt voidaan lopettaa.")

