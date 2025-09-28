import random
luku1 = random.randint(1, 10)

while True:
    luku2 = int(input("Arvaa luku!"))

    if luku1 < luku2:
        print("Liian suuri arvaus.")
    if luku1 > luku2:
        print("Liian pieni arvaus.")
    if luku1==luku2:
        print("Oikein!")
        break














