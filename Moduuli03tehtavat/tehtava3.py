hb = int(input("Paljonko hemoblobiiniarvosi on?"))
sukupuoli = str(input("Oletko mies vai nainen?"))
if sukupuoli == "mies" and hb < 134:
        print("Hemoglobiiniarvosi on alhainen.")
elif sukupuoli == "mies" and hb < 195 and hb > 134:
            print("Hemoglobiiniarvosi on normaali. ")
elif sukupuoli == "mies" and hb > 195:
            print("Hemoglobiiniarvosi on liian korkea. ")
elif sukupuoli == "nainen" and hb < 117:
    print("Hemoglobiiniarvosi on alhainen.")
elif sukupuoli == "nainen" and hb > 117 and hb < 175:
    print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli == "nainen" and hb > 175:
    print("Hemoglobiiniarvosi on liian korkea.")




