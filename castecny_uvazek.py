# Naše firma se rozhodla zaměstnávat i pracovníky na částečné úvazky,
# pro které bude vytvořena zvláštní třída. Vytvoř novou třídu PartTimeEmployee,
# která bude dědit od třídy Employee a bude mít navíc atribut workload (float),
# který reprezentuje velikost úvazku oproti plnému. Přidej informaci o úvazku k výpisu informací do funkce getInfo.

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

class PartTimeEmployee(Employee):
    def __init__(self,meno, pozice, rodne_cislo, id_zamestnance, probation, workload):
        super().__init__(meno, pozice, rodne_cislo, id_zamestnance, probation)
        self.workload = workload

    def getInfoUvazek(self):
        return super().getInfo() + f" a jeho uvazek je {self.workload}."


hanka = Employee("Janka","testerka",1234987,1368,False)
peter = Employee("Janka","testerka",9862763,130,True)
print(hanka.getInfo())
print(peter.getInfo())
zdenka = PartTimeEmployee("Zdenka","analytik",1234307,1009,False,0.75)
print(zdenka.getInfoUvazek())