
kevat=(3, 4, 5)
kesa=(6, 7, 8)
syksy=(9, 10, 11)
talvi=(12, 1, 2)

kuukausi =int(input("Anna haluamaasi kuukautta vastava numero(1-12), niin kerron, mikä vuodenaika on kyseessä."))
print(kuukausi)

if kuukausi in talvi:
    print("Kyseessä on talvi.")
elif kuukausi in kevat:
    print("Kyseessä on kevät.")
elif kuukausi in kesa:
    print("Kyseessä on kesä.")
else:
    print("Kyseessä on syksy.")








