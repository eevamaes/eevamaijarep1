#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä,
# nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä
# ilmoittaa tuloksen käyttäjälle.

#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.

luku1=int(input("Anna lemmikkimarsusi paino luoteina."))
print ("Joten marsu painaa nauloina:")
luku2=(int(32*luku1))
print (luku2)
print("Tämä on leivisköiksi muutettuna:")
luku3=(int(20*luku2))
print(luku3)
print(("Ja grammoina tämä tekee"), int(13.3*luku1))
print(("Ja edelleen kilogrammoina"), int(13.3*luku1/1000))

