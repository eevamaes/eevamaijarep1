import random
lkm= int(input("Anna noppasi tahkojen lukumäärä"))
def noppa():
    return random.randint(1, lkm)

silmaluku = noppa()
while silmaluku<lkm:
        print("Heitetään noppaa")
        silmaluku =noppa()
        print(silmaluku)
else:
    print("Saatiin suurin luku, nyt voidaan lopettaa.")
