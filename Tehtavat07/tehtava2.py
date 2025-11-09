nimet= set()

nimi=input("Anna jokin etunimi.")
while nimi not in nimet:
    nimet.add(nimi)

    print("Uusi nimi.")

    nimi = input("Anna jokin etunimi.")

    while nimi in nimet:
            print("Aiemmin syötetty nimi.")
            nimi=input("Anna jokin etunimi.")
    if nimi=="":
        break
print("Luettelemasi nimet ovat:")
for n in nimet:
    print(n)



