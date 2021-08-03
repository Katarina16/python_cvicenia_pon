class Zamestnanec:
    def vybrat_dovolenu(self, pocet_dni):
        if pocet_dni <= self.dny_dovolene:
            self.rodne_cislo = self.dny_dovolene - pocet_dni
            return "Uží si to"
        else:
            return "To je už moc"
    def vypisInformace(self):
        return f"Zamestnanec sa volá {self.jmeno} a pracuje na pozícií {self.pozicia}."
    def __init__(self, jmeno, pozice, rodne_cislo, id_zamestnance):
        self.jmeno = jmeno
        self.pozice = pozice
        self.rodne_cislo = rodne_cislo
        self.id_zamestnance = id_zamestnance
        self.dny_dovolene = 25
klára = Zamestnanec("Klára", "Nová","912346","23")
print(klára.vybrat_dovolenu(4))
# maria = Zamestnanec()
# maria.jmeno = "Maria Jablková"
# maria.pozicia = "Projektáčka"
# print(maria.vypisInformace())



# Zkus pro našeho nakladatele vytvořit software s využitím tříd a objektů.
# Vytvoř tedy třídu Book, která reprezentuje knihu. Každá kniha bude mít atributy title, pages a price.
# Hodnoty nastav ve funkci __init__.
# Přidej knize funkci getInfo, která vypíše informace o knize v nějakém pěkném formátu.
# Občas se stane, že se kniha moc neprodává a knihkupec se snaží nalákat kupující slevou.
# Přidej funkci discount, která bude mít jeden parametr - velikost slevy v procentech.
# Funkce sníží cenu knihy o dané procento.

# class Book:
#     def __init__(self, title, pages, price):
#         self.title = title
#         self.pages = pages
#         self.price = price
#
#     def getInfo(self):
#         return f"Kniha {self.title} má {self.pages} a jej cena je {self.price}."
#     def discount(self, sleva):
#         percento = (self.price/100)*sleva
#         return self.price-percento
# rybka = Book("Zlatá rybka", "130",199)
# print(rybka.discount(50))
# print(rybka.getInfo())

# Uvažuj, že navrhuješ software pro zásilkovou společnost.
# Vytvoř třídu Package, která bude mít tři atributy - address, weightInKilos a delivered.
# První dva atributy nastav pomocí parametrů funkce __init__.
# Parametr delivered nastav na začátku jako False.
# Připoj ke třídě funkci deliver, která změní hodnotu parametru delivered na True.
# Přidej funkci getInfo, která vypíše adresu, hmotnost a informaci o tom, zda byl balík již doručen.
# Zkus si vytvořit nějaké objekty ze třídy Package a ověř, že vše funguje.

# class Package:
#     def __init__(self, address, weightInKilos):
#         self.address = address
#         self.weightInKilos = weightInKilos
#         self.delivered = False
#
#     def getInfo(self):
#         return f"Balíček je v stave nedoručený, doručovacia adresa je {self.address} a jeho váha je {self.weightInKilos} kg."
#
#     def deliver(self):
#         self.delivered = True
#         return f"Balíček je v stave doručený, doručovacia adresa je {self.address} a jeho váha je {self.weightInKilos} kg."
#
# alza = Package("Vaclavské námestia 25",2)
# print(alza.getInfo())
# print(alza.deliver())



# U zaměstnanců budeme nově evidovat, jestli jsou ve zkušební době.
# Rozšiř funkci __init__ třídy Employee o parametr probation, který bude typu bool.
# Tuto hodnotu ulož jako atribut třídy Employee.
# Uprav funkci getInfo.
# Pokud je zaměstnanec ve zkušební době, přidej k jeho/jejímu výpisu text Je ve zkušební době.

# class Employee:
#     def __init__(self, meno, pozice, rodne_cislo, id_zamestnance, probation):
#         self.meno = meno
#         self.pozice = pozice
#         self.rodne_cislo = rodne_cislo
#         self.id_zamestnance = id_zamestnance
#         self.probation = probation
#
#     def getInfo(self):
#         if self.probation == True:
#          return f"Zamenstnanec {self.meno} je v skúšobnej dobe"
#         else:
#          return f"Zamenstnanec {self.meno} nie je v skúšobnej dobe"
#
# hanka = Employee("Janka","testerka",1234987,1368,False)
# peter = Employee("Janka","testerka",9862763,130,True)
# print(hanka.getInfo())
# print(peter.getInfo())

# Vytvoř třídu Auto, která bude obsahovat informace o autech, které půjčovna nabízí. Třída bude mít tyto atributy:
# registrační značka automobilu,
# značka a typ vozidla,
# počet najetých kilometrů,
# informaci o tom, jestli je vozidlo aktuálně volné (pravdivostní hodnota -- True pokud je volné
# a False pokud je vypůjčené).
# Vytvoř funkci __init__ pro třídu Auto. Registrační značku, značku
# a typ vozidla a počet kilometrů získej jako parametry funkce __init__ a ulož je jako atributy objektu.
# Poslední atribut nastav jako True, tj. na začátku je vozidlo volné.
# Vytvoř objekty, které reprezentují všechny automobily půjčovny.

class Auto:
    def __init__(self, spz, znacka, km):
        self.spz = spz
        self.znacka = znacka
        self.km = km
        self.dostupnost = True

    def getInfo(self):
        return f" {self.spz} {self.znacka} {self.km}"

    def pujc_auto(self):
        if self.dostupnost == True:
            self.dostupnost = False
            print("Potvrzuji zapůjčení vozidla")
        else:
            print(f"Vozidlo není k dispozici")

znackaAuta = input("Aké auto si prajete požičiať?: ")
peugeot = Auto("4A2 3020","Peugeot 403 Cabrio",47534)
octavia = Auto("1P3 4747","Škoda Octavia",41253)
print(peugeot.getInfo())
print(octavia.getInfo())

# Třídě Auto přidej metodu pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr.
# Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, změní hodnotu atributu, který určuje,
# zda je vozidlo půjčené, a vrátí text "Potvrzuji zapůjčení vozidla". Pokud je vozidlo již půjčené, vrátí text
# "Vozidlo není k dispozici".
# Dále tříde Auto přidej metodu get_info(), která vrátí informaci o vozidle
# (stačí registrační značka a značka a typ vozidla) jako řetězec.
# Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit.
# Uživatel může zadávat hodnoty Peugeot nebo Škoda. Jakmile si uživatel vybere značku,
# vypiš informaci o vozidle pomocí funkce get_info() a následně použij metodu pujc_auto.
# Dotaz na uživatele a výpis výsledků si v programu zkopíruj, abys dokázala otestovat,
# že funkce nedovolí půjčit stejné auto dvakrát.









