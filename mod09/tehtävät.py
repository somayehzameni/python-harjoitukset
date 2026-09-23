#tehtävä_1
class Auto:
    def __init__(self,rekisteritunnus,huippunopeus,tämänhetkinen_nopeus=0,kuljettu_matka=0):
        self.rekisteritunnus=rekisteritunnus
        self.hiuppunopeus=huippunopeus
        self.tämänhetkinen_nopeus=tämänhetkinen_nopeus
        self.kuljettu_matka=kuljettu_matka
    
Auto_1=Auto("ABC-123","142km/h")
print(Auto_1.rekisteritunnus,Auto_1.hiuppunopeus,Auto_1.tämänhetkinen_nopeus,Auto_1.kuljettu_matka)

#tehtävä_2
class Auto:
    def __init__(self,rekisteritunnus,hiuppunopeus,tämänhetkinen_nopeus=0,kuljettu_matka=0):
        self.rekisteritunnus=rekisteritunnus
        self.hiuppunopeus=hiuppunopeus
        self.tämänhetkinen_nopeus=tämänhetkinen_nopeus
        self.kuljettu_matka=kuljettu_matka
    def kiihdytä(self,nopeuden_muutokset):
            self.tämänhetkinen_nopeus=self.tämänhetkinen_nopeus+nopeuden_muutokset
            if self.tämänhetkinen_nopeus>self.hiuppunopeus:
                 self.tämänhetkinen_nopeus=self.hiuppunopeus
            elif self.tämänhetkinen_nopeus<0:
                 self.tämänhetkinen_nopeus=0
Auto_1=Auto("ABC-123",142)
Auto_1.kiihdytä(30)
Auto_1.kiihdytä(70)
Auto_1.kiihdytä(50)
print(f"Auton nopeus on nyt{Auto_1.tämänhetkinen_nopeus}")
Auto_1.kiihdytä(-200)
print(f"Auton nopeus on nyt{Auto_1.tämänhetkinen_nopeus}")

#Tehtävä_3:
class Auto:
    def __init__(self,rekisteritunnus,hiuppunopeus,tämänhetkinen_nopeus=0,kuljettu_matka=0):
        self.rekisteritunnus=rekisteritunnus
        self.hiuppunopeus=hiuppunopeus
        self.tämänhetkinen_nopeus=tämänhetkinen_nopeus
        self.kuljettu_matka=kuljettu_matka
    def kiihdytä(self,nopeuden_muutokset):
            self.tämänhetkinen_nopeus=self.tämänhetkinen_nopeus+nopeuden_muutokset
            if self.tämänhetkinen_nopeus>self.hiuppunopeus:
                 self.tämänhetkinen_nopeus=self.hiuppunopeus
            elif self.tämänhetkinen_nopeus<0:
                 self.tämänhetkinen_nopeus=0
    def kulje(self,tuntimäärän):
         self.kuljettu_matka=self.kuljettu_matka+(self.tämänhetkinen_nopeus*tuntimäärän)
Auto_1=Auto("ABC-123",142)
Auto_1.kiihdytä(60)
Auto_1.kulje(1.5)
print(f"kuljettu matka on {Auto_1.kuljettu_matka}")

#Tehtävä_4
import random
class Auto:
    def __init__(self,rekisterinumero,huippunopeus,tämänhetkinen_nopeus=0,kuljettu_matka=0):
        self.rekisterinumero=rekisterinumero
        self.huippunopeus=huippunopeus
        self.tämänhetkinen_nopeus=tämänhetkinen_nopeus
        self.kuljettu_matka=kuljettu_matka

    def kiihdytä(self,nopeuden_muutokset):
        if nopeuden_muutokset>0:
            self.tämänhetkinen_nopeus=self.tämänhetkinen_nopeus+nopeuden_muutokset
            if self.tämänhetkinen_nopeus>self.huippunopeus:
                self.tämänhetkinen_nopeus=self.huippunopeus
            else:self.tämänhetkinen_nopeus=self.tämänhetkinen_nopeus
        elif nopeuden_muutokset<0:
            self.tämänhetkinen_nopeus=self.tämänhetkinen_nopeus+nopeuden_muutokset
            if self.tämänhetkinen_nopeus<0:
                self.tämänhetkinen_nopeus=0
            else:
                self.tämänhetkinen_nopeus=self.tämänhetkinen_nopeus
    def kuljetu(self,tintimäärä):
        self.kuljettu_matka=self.kuljettu_matka+(self.tämänhetkinen_nopeus*tintimäärä)


def uusi_autot(kerrat):
    uusi_auto=[]
    for i in range(kerrat):
        huippunopeus=random.randint(100,200)
        rekisterinumero=f"ABC-{i+1}"
        new_car=Auto(rekisterinumero,huippunopeus)
        uusi_auto.append(new_car)
    return uusi_auto
lista=uusi_autot(10)
while True:
    voittaja_löytyi=False
    for auto in lista:
        auto.kiihdytä(random.randint(-10,15))
        auto.kuljetu(1)
    if any(auto.kuljettu_matka>=10000 for auto in lista):
        break
print(f"{"rekisterinumero" :<18} | {"huippunopeus" :<15} | {"tämänhetkinen_nopeus" :<24} | {"kuljettu_matka" :<16}")
print("-"*80)
for auto in lista:
    print(f"{auto.rekisterinumero :<18} | {auto.huippunopeus :<15} | {auto.tämänhetkinen_nopeus :<24} | {auto.kuljettu_matka :<16}")
            
        
