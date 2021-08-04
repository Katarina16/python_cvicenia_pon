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


# Pokračuj ve své práci pro streamovací službu. Služba nyní eviduje uživatele, kteří službu využívají.
# Vytvoř třídu Uzivatel, která bude mít atributy uzivatelske_jmeno a delka_sledovani,
# který udává celkovou délku pořadů, které uživatel zhlédl. Uživatelské jméno získej jako parametr
# a délka sledování je na začátku 0.
# Třídám Serial a Film přidej funkce get_celkova_delka(),
# která vrátí celkovou délku filmu/seriálu (u seriálu je to počet episod násobený délkou jedné episody).
# Třídě Uzivatel přidej funkci pripocti_zhlednuti(), která bude mít jeden parametr.
# Funkce zvýší atribut udávající celkovou délku sledování o zadaný parametr.
# Vytvoř objekt, který reprezentuje nějakého uživatele.
# Následně zkus uvažovat situaci, že uživatel zhlédne film a seriál, které jsi vytvořil(a) jako objekty.
# Uživateli připočti délky děl k délce sledování, využij k tomu funkci get_celkova_delka() u objektu a seriálu,
# abys zjistil(a), kolik minut (nebo hodin) videa celkem uživatel zhlédl.
# Nejjednodušší řešení je, pokud si u filmu/seriálu uložíš celkovou délku do pomocné proměnné
# a tuto pomocnou proměnnou potom předáš jako parametr funkci pripocti_zhlednuti().

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

    def get_celkova_delka(self):
        return self.delka

class Serial(Polozka):
    def __init__(self,nazov, zaner,pocetEpizod, delkaEpizody):
        super().__init__(nazov, zaner)
        self.pocetEpizod = pocetEpizod
        self.delkaEpizody = delkaEpizody

    def getInfo(self):
        return super().getInfo() + f" počet epizód: {self.pocetEpizod}, dĺžka epizódy: {self.delkaEpizody}."

    def get_celkova_delka(self):
        return self.pocetEpizod * self.delkaEpizody


class Uzivatel:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.delkaSledovani = 0

    def pripocti_zhlednuti(self, polozka):
        self.delkaSledovani += polozka.get_celkova_delka()
        return self.delkaSledovani

film1 = Film("Trhlina","Akčný",90)
print(film1.getInfo())
serial1 = Serial("Priatelia","Komédia",164,20)
print(serial1.getInfo())
film2 = Film("Únos","Akčný",80)
uzivatel1 = Uzivatel("Katka")
print(uzivatel1.pripocti_zhlednuti(film1))
print(uzivatel1.pripocti_zhlednuti(film2))


