tunnus= "python"
salasana= "rules"
kysymys1 = (input("Anna käyttäjätunnus, kiitos."))
kysymys2 = (input("Anna salasana, kiitos."))
tehdyt=0
maksimi=5

while kysymys1 != tunnus or kysymys2 != salasana:
    tehdyt = tehdyt + 1
    if tehdyt == maksimi:
        print("Pääsy evätty!")
        break
    kysymys1 =(input("Anna käyttäjätunnus, kiitos."))
    kysymys2 =(input("Anna salasana, kiitos."))
if kysymys1==tunnus and kysymys2==salasana:
        print("Tervetuloa!")










