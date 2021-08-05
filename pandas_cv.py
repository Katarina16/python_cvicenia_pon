import pandas
import wget
# datasety web kaggle
# wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/assets/nakupy.csv")
# nakupy = pandas.read_csv("nakupy.csv")
# print(nakupy.info())
# print(nakupy.shape) # vráti počet riadkov a počet stlpcov
#
# # print(nakupy.iloc[0:11])
#
# print(nakupy.iloc[1:4, 2:4])
#
# print(nakupy.iloc[:4, 2])
#
# radky = [2, 3]
# stlpce = [1, 3]
# print(nakupy.iloc[radky, stlpce])
#
# print(nakupy.head())
# print(nakupy.tail())


# Stáhni si soubor DataAnalyst.csv se seznamem nabídek práce pro datové analytiky.
# Soubor byl stažen z webu Kaggle.com, kde najdeš spoustu zajímavých dat, na kterých se můžeš učit, jak analyzovat data.
# Ale zpět k našim úkolům.
# Načti data do DataFrame, který si pojmenuj jobs.
# Nech si zobrazit názvy sloupců, které jsou v souboru uloženy.
# Podívej se, kolik má soubor řádek.
# Zjisti všechny informace o pracovní pozici na desátém řádku.
# Podívej se, kde budou pracovat zájemci vybraní na dvanáctou až dvacátou pozici.

#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/excs/nabidky/assets/DataAnalyst.csv")
# jobs = pandas.read_csv("DataAnalyst.csv")
#
# print(jobs.info()) # Nech si zobrazit názvy sloupců, které jsou v souboru uloženy.
# print(jobs.columns)
#
# print(jobs.shape[0]) #pocet riadkov
# print(jobs.shape[1]) #pocet stlpcov
#
# print(jobs.info())
# print(jobs.iloc[12:21, 6]) # Podívej se, kde budou pracovat zájemci vybraní na dvanáctou až dvacátou pozici.
# print(jobs.Location[11:21])# Podívej se, kde budou pracovat zájemci vybraní na dvanáctou až dvacátou pozici.

#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/assets/staty.json")
staty = pandas.read_json("staty.json")
staty.to_csv("staty.csv") #konvertovat do formátu csv

print(staty.info())
staty = staty.set_index("name")

print(staty.loc["Czech Republic"])

print(staty.loc[:"Estonia","area"])
print(staty.area)
print(staty.head())

print(type(staty)) #vráti typ premenej

area = staty["area"]

print(area.sum())

print(staty["population"].sum())

print(staty["population"] < 1_000_000)  #cislo sa dá naspísať aj bez podtržítek ale pomucka pre nás, aby sme sa v ňom vyznali

print(sum(staty["population"] < 1_000_000)) #kolko statov ma menje obyvateľov ako 1 milión

male_staty = staty["population"] < 1_000_000

print(staty[male_staty]["area"])

# male_europske_staty = staty[
#     (staty["population"] < 1_000_000) &
#     (staty["region"] == "Europe")
# ]

male_eur_asie_staty = staty[
    (staty["population"] < 1_000_000) &
    (staty["region"].isin(["Europe","Asia"])) #víc hodnot v stlpci isin()
]

print(male_eur_asie_staty)












