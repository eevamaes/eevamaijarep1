import random
summa =0

lkm= int(input("Anna noppien lukumäärä."))
print("Heitetään jokaista noppaa kerran:")
for noppa in range(lkm):

    noppa=random.randint(1,6)
    print(noppa)

    summa+=noppa


print("Silmälukujen yhteenlaskettu summa on", summa)


















