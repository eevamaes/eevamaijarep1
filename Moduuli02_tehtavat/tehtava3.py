#Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
# Ohjelma tulostaa suorakulmion piirin ja pinta-alan. Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

luku1=float(input ("Mikä on suorakulmion kanta? Ilmoita senttimetreinä."))
luku2=float(input ("Mikä on suorakulmion korkeus? Ilmoita senttimetreinä."))

#suorakulmion piiri saadaan laskemalla yhteen kaikki neljä sivua, eli kanta+korkeus+kanta+korkeus

print(("Joten suorakulmion piiri on "), float(luku1+luku2+luku1+luku2), ("cm"))

#suorakulmion pinta-ala saadaan kertomalla kanta ja korkeus keskenään.

print(("Ja suorakulmion pinta-ala on "), float(luku1*luku2), ("cm2"))