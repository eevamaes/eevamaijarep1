#Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

a=int(input("Anna valitsemasi kokonaisluku."))
b=int(input("Anna toinen valitsemasi kokonaisluku."))
c=int(input("Anna vielä kolmas valitsemasi kokonaisluku."))

print("Lasketaan nyt näiden kolmen luvun summa")
print(a+b+c)

print("Lasketaan seuraavaksi näiden kolmen luvun tulo.")
print(a*b*c)

print("Lasketaan vielä näiden kolmen luvun keskiarvo.")
print(f"{(a*b*c)/3:.2f}")