def gallona(määrä):
    litrat=määrä*3.785
    return litrat

määrä=int(input("Montako gallonaa sinulla on bensaa?"))

while määrä>=0:
    print("Se tekee", gallona(määrä), "litraa.")
    määrä = int(input("Montako gallonaa sinulla on bensaa?"))
if määrä < 0:
    print("En jaksa kysellä enempää.")








