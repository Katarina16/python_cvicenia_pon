# Uvažuj, že vyvíjíš software pro službu, která nabízí streamování videa.
# Služba nabízí dva typy pořadů - filmy a seriály. Firma chce evidovat, které filmy a seriály nabízí a jejich žánry.
# Dále chce u filmů evidovat délku a u seriálů počet episod a délku jedné episody.
# Vytvoř program, který bude obsahovat tři třídy - Polozka, Film a Serial.
# Třída Polozka bude sloužit jako základ pro další třídy. Bude mít atributy určující název a žánr.
# Oba atributy nastav ve funkci __init__(), žánr získej jako parametr funkce.
# Třída Film bude potomkem třídy Polozka. Film má kromě názvu a žánru atribut délka.
# Třída Serial bude potomkem třídy Polozka. Má kromě názvu a žánru atributy počet epizod a délka epizody.
# Všem třídám přidej funkci get_info(), která vypíše informace o položce, resp. o filmu a seriálu.
# Funkce u třídy Polozka vypíše název a žánr.
# Následně tuto funkci využij ve funkcích u tříd Film a Serial a přidej k ní informaci o délce, resp. počtu episod.
# Pro naprogramování si vytvoř alespoň jeden objekt reprezentující film a seriál a ověr, že vše funguje.

class Polozka:
    def __init__(self, nazov, zaner):
        self.nazov = nazov
        self.zaner = zaner

    def getInfo(self):
        return f"Název: {self.nazov}, žáner: {self.zaner}."

class Film(Polozka):
    def __init__(self, nazov, zaner, delka):
        super().__init__(nazov,zaner)
        self.delka = delka

    def getInfo(self):
        return super().getInfo() + f" délka: {self.delka}."

class Serial(Polozka):
    def __init__(self,nazov, zaner,pocetEpizod, delkaEpizody):
        super().__init__(nazov, zaner)
        self.pocetEpizod = pocetEpizod
        self.delkaEpizody = delkaEpizody

    def getInfo(self):
        return super().getInfo() + f" počet epizód: {self.pocetEpizod}, dĺžka epizódy: {self.delkaEpizody}."

film1 = Film("Trhlina","Akčný","90 minút")
print(film1.getInfo())
film2 = Serial("Priatelia","Komédia",164,"20 minút")
print(film2.getInfo())
