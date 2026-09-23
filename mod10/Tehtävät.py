#tehtävä_1,2,3


class Hissi:
    def __init__(self,alimman_kerroksen_numero,ylimmän_kerroksen_numero):
        self.alimman_kerroksen_numero=alimman_kerroksen_numero
        self.ylimmän_kerroksen_numero=ylimmän_kerroksen_numero
        self.nykyinen_kerros_numero=self.alimman_kerroksen_numero
    def ylä_kerros(self,):
        self.nykyinen_kerros_numero=self.nykyinen_kerros_numero+1
        print(f"Hissi nyt on {self.nykyinen_kerros_numero}")

    def ala_kerros(self,):
        self.nykyinen_kerros_numero=self.nykyinen_kerros_numero-1
        print(f"Hissi nyt on {self.nykyinen_kerros_numero}")

    def sirry_kerrokseen(self,numero):
        print(f"siirrytään kerokseen {numero}")
        while numero!=self.nykyinen_kerros_numero:
            
            if numero>self.nykyinen_kerros_numero:
                self.ylä_kerros()
            elif numero<self.nykyinen_kerros_numero:
                self.ala_kerros()
        print("saaput halumaan kerokseen")


class Talo:
    def __init__(self,alimman_kerroksen_numero,ylimmän_kerroksen_numero,hissin_lukumäärä):
        self.alimman_kerroksen_numero=alimman_kerroksen_numero
        self.ylimmän_kerroksen_numero=ylimmän_kerroksen_numero
        self.hissin_lukumäärä=hissin_lukumäärä


        self.hissin_tiedot=[]
        for i in range(hissin_lukumäärä):
            uusi_hissi=Hissi(self.alimman_kerroksen_numero,self.ylimmän_kerroksen_numero)
            self.hissin_tiedot.append(uusi_hissi)
    def aja_hissiä(self,index,numero) : 
        kyseinen_hissi=self.hissin_tiedot[index]
        print(f"nyt käytetään hissi numero{index}")
        kyseinen_hissi.sirry_kerrokseen(numero)
    def palohälytys(self,):
        print("kaikki hisiit täytty siirtyä pohgjakerrokseen")
        for i in self.hissin_tiedot:
            i.sirry_kerrokseen(self.alimman_kerroksen_numero)


uusi_hissi=Talo(1,10,4)

uusi_hissi.aja_hissiä(2,5)
uusi_hissi.aja_hissiä(2,1)

uusi_hissi.palohälytys()

#tehtävä_4

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

class Kilpailu:
    def __init__(self,kilpailun_nimi,pituus,osalistuvien_autojen_lista):
        self.kilpailun_nimi=kilpailun_nimi
        self.pituus=pituus
        self.osalistuvien_autojen_lista=osalistuvien_autojen_lista
    def tunti_kuluu(self):
        for auto in self.osalistuvien_autojen_lista:
            auto.kiihdytä(random.randint(-10,15))
            auto.kuljetu(1)
    def tulostaa_tilanne(self):
        print(f"{"rekisterinumero" :<18} | {"huippunopeus" :<15} | {"tämänhetkinen_nopeus" :<24} | {"kuljettu_matka" :<16}")
        print("-"*80)
        for auto in self.osalistuvien_autojen_lista:
            print(f"{auto.rekisterinumero :<18} | {auto.huippunopeus :<15} | {auto.tämänhetkinen_nopeus :<24} | {auto.kuljettu_matka :<16}")
    def kipailu_ohi(self):
        for auto in self.osalistuvien_autojen_lista:
            if auto.kuljettu_matka>=self.pituus:
                return True
            
            return False
            


def uusi_autot(kerrat):
    uusi_auto=[]
    for i in range(kerrat):
        huippunopeus=random.randint(100,200)
        rekisterinumero=f"ABC-{i+1}"
        new_car=Auto(rekisterinumero,huippunopeus)
        uusi_auto.append(new_car)
    return uusi_auto

lista=uusi_autot(10)
kilpailu_1=Kilpailu("Suuri romuralli",8000,lista)  
tuntit=0
while kilpailu_1.kipailu_ohi==False:
    kilpailu_1.tunti_kuluu()
    tuntit=tuntit+1

    if tuntit%10==0:
        kilpailu_1.tulostaa_tilanne()
kilpailu_1.tulostaa_tilanne()    



