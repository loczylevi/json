"""
Fő Feladat: RPG Karakterkezelő Program

Leírás: Írj egy programot, amely egy RPG (szerepjáték) karakterekből álló JSON fájlt használ. 
A program töltse be a karaktereket, majd hozzon létre belőlük Python objektumokat. A karakterek különböző tulajdonságokkal rendelkeznek, 
mint például név, szint, életerő, támadóerő és védekezés.

Cél: A karakterek használatával tudj szimulálni egy egyszerű harcot.

Lépések:

1. Töltsd be a JSON adatokat:
   - A JSON fájlt olvasd be, és alakítsd Python adatstruktúrává.

2. Hozz létre egy Character osztályt:
   - Minden karaktert egy Character osztály reprezentáljon.
   - Az osztály tartalmazza a következő attribútumokat: név, szint, életerő, támadóerő, védekezés.
   - Implementálj egy take_damage metódust, amely csökkenti a karakter életerejét egy adott sebzés alapján.

3. Készíts harci logikát:
   - Írj egy fight függvényt, amely két karakter objektumot vesz be, és kiszámítja a harcot.
   - A harci logika legyen egyszerű: a támadó karakter támadóerejéből vond ki a védekező karakter védekezését, 
     majd ezt a sebzést alkalmazd a védekező karakter életerejére a take_damage metódussal.

4. Szimuláld a harcot:
   - Két karaktert válassz ki a JSON adatbázisból, és szimulálj egy harcot közöttük, amíg valamelyik karakter életereje nullára csökken."""

import json
with open("adat.json","r",encoding="UTF-8") as f:
    adat = json.load(f)


#print(type(adat))

class Karakterek:
    def __init__(self, nev, szint, eletero, tamadoero, vedekezes):
        self.nev = nev
        self.szint = szint
        self.eletero = eletero
        self.tamadoero = tamadoero
        self.vedekezes = vedekezes
        self.alive = True
    def take_damage(self, w2, tenyleges_sebzes):
        sebzes =  w2.eletero - tenyleges_sebzes 
        print(f" {w2.eletero}hp - {tenyleges_sebzes}att = {sebzes}")
        if w2.eletero <= 0:
            c = w2.alive = False
            return c
        else:
            return sebzes
            
            
            
        
    def harc(self, w1, w2):
        direct_hit = w1.tamadoero - w2.vedekezes
        print(f"{w1.tamadoero} att - {w2.vedekezes}def= {direct_hit}")
        return direct_hit
        
#print(adat["characters"][0]['name'])

lista = []
for szam in range(len(adat['characters'])):
    meghivo = Karakterek(adat["characters"][szam]["name"],adat["characters"][szam]["level"],adat["characters"][szam]["health"], adat["characters"][szam]["attack"],adat["characters"][szam]["defense"])
    lista.append(meghivo)

harcos1 = lista[0]
harcos2 = lista[1]
harcos3 = lista[2]


with open("gaming.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(adat,indent=4))

with open("gaming.json", "r", encoding="utf-8") as f:
    gayming = json.load(f)

    

import time
while harcos1.alive == True:
    time.sleep(1)
    print(f"'{harcos1.nev}' támadja --> '{harcos2.nev}' ")
    print(f"{harcos1.nev}: attack: {harcos1.tamadoero} HP: {harcos1.eletero}")
    print(f"{harcos2.nev}: attack: {harcos2.tamadoero} HP: {harcos2.eletero}\n________________________________________________________________________________________________________________")
    vedekezes_levonas = harcos1.harc(harcos1, harcos2)
    print(vedekezes_levonas)
    print("______________________________________________________________")
    sebzes_levonas = harcos1.take_damage(harcos2, vedekezes_levonas)
    print(sebzes_levonas)
    #print(type(gayming))
    gayming["characters"][1]['health'] = gayming["characters"][1]['health'] - sebzes_levonas
    time.sleep(1)
    print(f'HP_ {gayming["characters"][1]["health"]}')
    with open("gaming.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(gayming, indent=4))
    
    print(harcos2.alive)
    time.sleep(5)
    
    
    

    









"""
print("\n")
print(adat["characters"][0]["health"])

adat["characters"][0]["health"] = 70

print(adat["characters"][0]["health"])
"""
    





