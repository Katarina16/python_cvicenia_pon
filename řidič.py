# Pokračuj ve své práci pro zásilkovou společnost. Společnost nyní eviduje jednotlivé řidiče
# a eviduje balíky, které má každý řidič doručit.
# Vytvoř třídu Driver, která má dva atributy: name (jméno řidiče) a packageList (seznam balíků k doručení,
# na začátku je prázdný).
# Přidej třídě funkci assignPackage, která bude mít jeden parametr - package (balík k doručení,
# může se jednat i o cenný balík). Funkce nejprve zkontroluje, zda balík již nebyl doručen.
# Pokud ano, vypíše funkce text: "Nelze přiřadit, balík již byl doručen."
# Pokud balík ještě nebyl doručen, je přidán do seznamu balíků packageList (použij funkci append).
# U řidiče chceme sledovat, kolik by měl ještě doručit balíků. Napiš funkci remainingPackages,
# která vrátí počet balíků, které má řidič přiřazené a ještě je nedoručil.

class Package:
    def __init__(self, address, weightInKilos):
        self.address = address
        self.weightInKilos = weightInKilos
        self.delivered = False

    def getInfo(self):
        return f"Balíček je v stave {self.delivered}, doručovacia adresa je {self.address} a jeho váha je {self.weightInKilos} kg."

    def deliver(self):
      self.delivered = True

class ValuablePackage(Package):
    def __str__(self):
        return super().getInfo() + f" a jeho hodnota je {self.value}."

    def __init__(self,address, weightInKilos,value):
        super().__init__(address, weightInKilos)
        self.value = value

class Driver(Package):
    def __init__(self, address, weightInKilos, name):
        super().__init__(address, weightInKilos,)
        self.name = name
        self.zoznamBalickov = []

    def assignPackage(self, package):
        if self.delivered:
            return f"Balíček už bol doručený"
        else:
            self.zoznamBalickov.append(package)
            # return len(self.zoznamBalickov)

    def remainingPackages(self):
        pocetBaliku = 0
        for polozka in self.zoznamBalickov:
            if self.delivered == False:
                pocetBaliku += 1
        # return len(self.zoznamBalickov)


alza = Package("Vaclavské námestia 25",2)
datart = Package("Lenovo", 2.5)
print(alza.getInfo())
print(alza.deliver())
balicek = ValuablePackage("Jeseniova 212",0.5, 250)
print(balicek.__str__())
posta = Driver("Jeseniova 212",0.5, "Česká pošta")
posta.assignPackage(alza)
posta.assignPackage(datart)
print(posta.remainingPackages())
