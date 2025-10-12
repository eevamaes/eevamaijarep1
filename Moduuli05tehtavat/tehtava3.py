luku= int(input("Anna jokin luku."))
for numero in range (2,luku):

        if luku % numero ==0:
            print("Tämä ei ole alkuluku")
            break
else:
    print("Tämä on alkuluku. JEE!")




