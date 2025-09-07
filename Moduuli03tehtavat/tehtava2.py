hytti: str=(input("Minkä hyttiluokan haluat valita, A, B, C vai "
                            "LUX?"))

if hytti == "A" or hytti == "a":
    print("Siis A, ikkunallinen hytti autokannen yläpuolella.")
elif hytti == "B" or hytti == "b":
    print("Siis B, ikkunaton hytti autokannen yläpuolella.")
elif hytti == "C" or hytti == "c":
    print("Siis C, ikkunaton hytti autokannen alapuolella.")
elif hytti == "LUX" or hytti == "lux":
    print("Siis LUX, eli parvekkeellinen hytti yläkannella.")
else:
    print("Virheellinen hyttiluokka!")



