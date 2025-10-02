luvut=[]
luku=input("Anna jokin luku tai paina Enteriä.")

while luku!="":
    numero = int(luku)
    luvut.append(numero)
    luku=input("Anna jokin luku tai paina Enteriä.")


luvut.sort(reverse=True)
print("Tulostetaan viisi suurinta lukua suurimmasta pienimpään:", luvut[:5])





