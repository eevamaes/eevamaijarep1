koodit= {"UUDD": "Moskova_Domodedovo",
         "ULLI": "Pietari_Pulkovo",
         "EGLL": "Lontoo_Heathrow"}
for k in koodit.keys():
    print(f"{k}: {koodit[k]}")

uusi=input("Haluatko lisätä listaan uuden lentokentän, kyllä vai ei?")
while uusi =="kyllä":
    kentta=input("Anna uuden kentän nimi")
    icao=input("Anna uuden kentän ICAO-koodi")
    koodit[icao] = kentta
    for icao, kentta in koodit.items():
        print(f"{icao}: {kentta}")
    uusi=input("Haluatko lisätä listaan uuden lentokentän, kyllä vai ei?")
while uusi =="ei":
        haku=input("Jos haluat tietää jotakin ICAO-koodia vastaavan kentän nimen, anna koodi, "
        "tai paina enteriä, jos haluat lopettaa.")
        if haku =="":
            print("Lopetetaan siis.Tässä vielä lentokenttien lista:")
            for icao, kentta in koodit.items():
                print(f"{icao}: {kentta}")
            break
        else:
            print(f"Se on {koodit[haku]}.")
            uusi = input("Haluatko lisätä listaan uuden lentokentän, kyllä vai ei?")
            while uusi == "kyllä":
                kentta = input("Anna uuden kentän nimi")
                icao = input("Anna uuden kentän ICAO-koodi")
                koodit[icao] = kentta
                for icao, kentta in koodit.items():
                    print(f"{icao}: {kentta}")
                uusi = input("Haluatko lisätä listaan uuden lentokentän, kyllä vai ei?")









