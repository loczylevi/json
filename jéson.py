"""

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["city"])


import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

"""

"""

1. Feladat: JSON adat betöltése és kiírása
   Leírás: Írj egy Python szkriptet, amely betölt egy JSON formátumú fájlt és kiírja annak tartalmát a konzolra.
   Lépések:
      - Nyiss meg egy JSON fájlt olvasásra.
      - Használd a json.load() függvényt az adatok betöltéséhez.
      - Írasd ki az adatokat a konzolra.
"""
import json

with open("sample_data_hu.json", "r" ) as f:
    adat = json.load(f)

print(type(adat))

print(adat["persons"])



"""
2. Feladat: JSON adat módosítása és mentése
   Leírás: Készíts egy programot, amely betölt egy JSON fájlt, módosít benne egy kulcs értékét, majd elmenti az adatot egy új fájlba.
   Lépések:
      - Nyisd meg a JSON fájlt olvasásra és töltsd be az adatokat.
      - Módosíts egy megadott kulcs értékét.
      - Írd vissza az adatokat egy új JSON fájlba.
"""
import json

with open("sample_data_hu.json", "r", encoding="UTF-8" ) as f:
    adat = json.load(f)

print(type(adat))

print(adat["persons"])



adat["persons"][1]["name"] = "SZABI INTERFACE"

with open("megvaltoztatott.json", "w", encoding="latin2") as f:
    print(json.dumps(adat,indent=4, sort_keys=True), file=f,end="\n")


print("\n",adat["persons"])


"""
3. Feladat: JSON adat szűrése
   Leírás: Írj egy programot, amely betölt egy JSON fájlt, amely egy személyek listáját tartalmazza, majd szűrd ki azokat, akik egy adott városban élnek.
   Lépések:
      - Töltsd be a JSON fájlt, amely személyeket tartalmaz.
      - Használj listakomprehensziót vagy filter függvényt a szűréshez.
      - Írasd ki az eredményt.
"""

import json

with open("sample_data_hu.json", "r", encoding="UTF-8" ) as f:
    adat = json.load(f)
    
    
bekeres = input("Szürendő város:\t")

kereso = [print(f"Találat:\t{json.dumps(sor, indent=3)}") for sor in adat["persons"] if bekeres in sor["city"]]



with open("uj.json","w",encoding="utf-8") as f:
    print(kereso, file=f)












