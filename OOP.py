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

class Package:
    def __init__(self, address, weightInKilos):
        self.address = address
        self.weightInKilos = weightInKilos
        self.delivered = False

    def getInfo(self):
        return f"Balíček je v stave nedoručený, doručovacia adresa je {self.address} a jeho váha je {self.weightInKilos} kg."

    def deliver(self):
        self.delivered = True
        return f"Balíček je v stave doručený, doručovacia adresa je {self.address} a jeho váha je {self.weightInKilos} kg."

alza = Package("Vaclavské námestia 25",2)
print(alza.getInfo())
print(alza.deliver())



# U zaměstnanců budeme nově evidovat, jestli jsou ve zkušební době.
# Rozšiř funkci __init__ třídy Employee o parametr probation, který bude typu bool.
# Tuto hodnotu ulož jako atribut třídy Employee.
# Uprav funkci getInfo.
# Pokud je zaměstnanec ve zkušební době, přidej k jeho/jejímu výpisu text Je ve zkušební době.

class Employee:
    def __init__(self, meno, pozice, rodne_cislo, id_zamestnance, probation):
        self.meno = meno
        self.pozice = pozice
        self.rodne_cislo = rodne_cislo
        self.id_zamestnance = id_zamestnance
        self.probation = probation

    def getInfo(self):
        if self.probation == True:
         return f"Zamenstnanec {self.meno} je v skúšobnej dobe"
        else:
         return f"Zamenstnanec {self.meno} nie je v skúšobnej dobe"

hanka = Employee("Janka","testerka",1234987,1368,False)
peter = Employee("Janka","testerka",9862763,130,True)
print(hanka.getInfo())
print(peter.getInfo())







