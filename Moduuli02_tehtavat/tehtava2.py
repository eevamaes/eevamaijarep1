#Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan


luku1=int(input ("Mikä on ympyrän säde?"))
print (luku1, "cm")
print ("Ympyrän pinta-ala on A=πr2, jossa r on säde")

import math

(print ("Eli tässä tapauksessa "),
 print ((f"{math.pi*luku1**2:.2f}"), "cm2"))