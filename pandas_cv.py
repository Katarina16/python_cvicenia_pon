import pandas
import wget
# datasety web kaggle
# wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/assets/nakupy.csv")
nakupy = pandas.read_csv("nakupy.csv")
print(nakupy.info())
print(nakupy.shape) # vráti počet riadkov a počet stlpcov
