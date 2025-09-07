vuosi = int(input("Anna vuosiluku."))
if vuosi %100==0 and vuosi %400 !=0:
        print("Kyseessä ei ole karkausvuosi.")
elif vuosi %4==0:
            print("Kyseessä on karkausvuosi.")

else:
    print("Kyseessä ei ole karkausvuosi.")