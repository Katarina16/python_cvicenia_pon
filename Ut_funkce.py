import math
import random

def pozdrav_uzivatele(osloveni1, osloveni2):
    print(f"Ahoj {osloveni1, osloveni2}")
pozdrav_uzivatele('Betko','Majka')

def secti_cisla(a,b):
    return a + b

vysledek = secti_cisla(3,6)
print(vysledek)

# ak parameter napr bonus=0, je to nepovinny parameter, za nepovinný sa nedá dať povinný, iba ďalší nepovinný
# def zjisti_znamku(points):
#   if points <= 60:
#     mark = 5
#   elif points <= 70:
#     mark = 4
#   elif points <= 80:
#     mark = 3
#   elif points <= 90:
#     mark = 2
#   else:
#     mark = 1
#   return mark
# pocet_bodu = int(input("Zadej pocet bodu"))
# znamka = zjisti_znamku(pocet_bodu)
# if znamka == 5:
#   body_opravny_pokus = int(input("Zadej body z opravného pokusu:"))
#   znamka_opravny_pokus = zjisti_znamku(body_opravny_pokus)
# print("Vysledna znamka je", znamka)
# print(f"Vysledna znamka je {znamka}")


#Napište funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek.

def mult(a, b):
  return a * b
print(mult(3,6))

#Napiš funkci totalPrice, která vypočte cenu noci v hotelu. Funkce bude mít dva parametry - persons a breakfast.
#Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč. Funkce vrátí výslednou cenu.
#Parametr breakfast je nepovinný a výchozí hodnota je False.
#Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. totalPrice(3), totalPrice(2, True).

def totalPrice(persons, breakfast=False):
  if breakfast == False:
   cena = persons*850
   print(cena)
   # return persons * 850
  else:
   cena_ranajky = ((persons*850)+(persons*125))
   print(cena_ranajky)
   # return persons * 925

totalPrice(3,False)
totalPrice(1,True)
totalPrice(2)

# def TotalPrice(person, breakfast=False):
#    return person * (850 + 125 * breakfast)

# Napiš funkce monthOfBirth, která bude mít jeden parametr - rodné číslo.
# Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup.
# Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.
# Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.

def monthOfBirth(rodneCislo):
  mesiac = int(rodneCislo[2:4]) #udela to dvojku, trojku a 4 sa nepočíta
  if mesiac >= 51:
    mesiac -= 50
    print(mesiac)
  else:
    print(mesiac)

# def monthOfBirth(rodneCislo):
#   mesiac = int(rodneCislo[2:4])
# return month %  50

monthOfBirth("9555125899")
monthOfBirth("9207054439")

# def monthOfBirth(rodneCislo):
#   mesiac = int(rodneCislo[2:4])

# Napiš funkci, která bude jednoduchou simulací rulety. Budeme uvažovat pouze možnost sázení na řady.
# Uživatel si může vybrat jednu ze tří řad:
# první řada (hodnoty 1, 4, 7 atd.),
# druhá řada (hodnoty 2, 5, 8 atd.),
# třetí řada (hodnoty 3, 6, 9 atd.).
# Zeptej se uživatele, na kterou ze tří řad sází a na výši sázky.
# Vytvoř funkci roulette, která bude mít parametry číslo řady a výši sázky.
# Pomocí funkce randint z modulu random vygeneruj náhodné číslo v rozsahu od 0 (včetně) do 36.
# Vyhodnoť, do které řady číslo náleží. Nezapomeň, že 0 nepatří do žádné z řad a pokud padne, uživatel vždy prohrává.
# Funkce roulette vrací hodnotu výhry. Pokud uživatel vsadil na správnou řadu, vyhrává dvojnásobek sázky,
# v opačném případě nevyhrává nic jeho sázka propadá.


# prva = [1, 3, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
# druha = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
# tretia = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
# rada = int(input("Zadej číslo rady: "))
#
# def roulette (cislo, rada):
#     if rada == 1 and cislo in prva:
#         return True
#     if rada == 2 and cislo in druha:
#         return True
#     if rada == 3 and cislo in tretia:
#         return True
# rada = int(input("Zadej radu: "))
# cislo = random.randint(0, 36)
# print(f"Padlo čislo {cislo}")
# print(roulette(2,2))



# První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné
# (pokud je na začátku předvolba "+420").
# Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
# Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.



def overCislo(cislo):
    delka = len(cislo)
    if delka == 9 or (delka == 13 and delka[0:4] == "+420"):
        print("Platné číslo")
    else:
        print("Neznáme číslo")
def cena_spravy(sprava):
    return math.ceil(len(sprava) / 180) * 3


cislo = input("Zadaj telefóne číslo: ")
sprava = input("Zadaj text správy: ")
print(f"Cena správy je {cena_spravy(sprava)}")





