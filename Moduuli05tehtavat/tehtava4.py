lista=[]

while len(lista) <5:
    kaupunki = input("Nimeä jokin suomalainen kaupunki.")
    lista.append(kaupunki)

    if len(lista)==5:
        break
print("")
print("Viisi nimeämääsi kaupunkia ovat siis:")
print("")
for tulos in lista:
    print(tulos)








