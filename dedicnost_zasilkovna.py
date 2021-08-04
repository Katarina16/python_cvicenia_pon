# Pokračuj ve své práci pro zásilkovou společnost. Společnost nově doručuje i cenné balíky,
# které mají zadanou určitou hodnotu.
# Vytvoř třídu ValuablePackage, která dědí od třídy Package. ValuablePackage
# má navíc atribut value, ostatní atributy dědí od třídy Package.
# Atribut value nastav pomocí funkce __init__. Ostatní parametry předej funkci __init__ třídy Package.
# Vytvoř si alespoň jeden objekt a zkus volání jeho funkcí.

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

alza = Package("Vaclavské námestia 25",2)
print(alza.getInfo())
print(alza.deliver())
balicek = ValuablePackage("Jeseniova 212",0.5, 250)
print(balicek.__str__())