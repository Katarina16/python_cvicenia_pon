class Zamestnanec:
    def vybrat_dovolenu(self, pocet_dni):
        if pocet_dni <= self.dny_dovolene:
            self.rodne_cislo = self.dny_dovolene - pocet_dni
            return "Uží si to"
        else
            return "To je už moc"
    def vypisInformace(self):
        return f"Zamestnanec sa volá {self.jmeno} a pracuje na pozícií {self.pozicia}."
    def __init__(self, jmeno, pozice, rodne_cislo, id_zamestnance):
        self.jmeno = jmeno
        self.pozice = pozice
        self.rodne_cislo = rodne_cislo
        self.id_zamestnance = id_zamestnance
        self.dny_dovolene = 25

maria = Zamestnanec()
maria.jmeno = "Maria Jablková"
maria.pozicia = "Projektáčka"
print(maria.vypisInformace())