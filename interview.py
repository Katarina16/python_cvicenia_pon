# Uvažuj následující třídu Kontakt, která slouží k evidenci všech kontaktů
# (např. zákazníků, zaměstnanců, uchazečů o práci atd.).
# class Kontakt:
#   def __init__(self, jmeno, email):
#     self.jmeno = jmeno
#     self.email = email
# Vytvoř třídu Uchazec, která bude dědit od třídy Kontakt a která reprezentuje uchazeče o práci.
# Uchazeč o práci bude mít navíc atribut datum_pohovoru a zapis_z_pohovoru.
# Datum pohovoru objekt získá z parametru a zápis z pohovoru je na začátku prázdný řetězec "".
# Dále přidej funkci uloz_zapis(), která bude mít jako parametr textový zápis pohovoru.
# Tato funkce ohlídá, zda uživatel omylem nezadává zápis k pohovoru, který ještě neproběhl.
# Na začátku funkce porovnej aktuální datum a datum pohovoru.
# Pokud podle data pohovor ještě neproběhl, vrať chybový text, který informuje uživatele o chybě.
# Pokud již podle data pohovor proběhl, ulož zápis a vrať text s informací, že zápis byl uložen.
import  datetime
from datetime import datetime


class Kontakt:
    def __init__(self, jmeno, email):
        self.jmeno = jmeno
        self.email = email


class Uchazec(Kontakt):
    def __init__(self, jmeno, email, datum_pohovoru):
        super().__init__(jmeno, email)
        self.datum_pohovoru = datum_pohovoru
        self.zapis_z_pohovoru = ""

    def uloz_zapis(self, zapis):
        if datetime.now() > self.datum_pohovoru:
            self.zapis_z_pohovoru = zapis
            print('Zapis ulozen.')
        else:
            print('[ERROR] Pohovor jeste neprobehl.')


datum_pohovoru_OK = datetime(2020, 10, 25)
datum_pohovoru_NOK = datetime(2022, 10, 25)

uchazec = Uchazec('Andy', 'example@email.com', datum_pohovoru_OK)
uchazec.uloz_zapis("Prijat")

uchazec = Uchazec('Andy', 'example@email.com', datum_pohovoru_NOK)
uchazec.uloz_zapis("Prijat")



