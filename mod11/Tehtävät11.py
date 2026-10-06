#Tehtävä_1(Periytyminen)
class Julkaisu:
    def __init__(self,nimi):
        self.nimi=nimi
    def tulosta_tiedot(self):
        print(f"Julkaisu on {self.nimi}")
class Kirja(Julkaisu):
    def __init__(self,nimi,kirjoittaja,sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja=kirjoittaja
        self.sivumäärä=sivumäärä
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"kirjoittaja on {self.kirjoittaja} ja  sivumäärä on {self.sivumäärä}")
class Lehti(Julkaisu):
    def __init__(self,nimi,päätoimintoja):
        super().__init__(nimi)
        self.päätoimintoja=päätoimintoja
    def tulosta_tiedot(self):
            super().tulosta_tiedot()
            print(f" päätoimintaja on{self.päätoimintoja}")
    
lehti=Lehti("Aku Ankka","Aki Hyyppä")
kirja=Kirja("Hytti n:o 6","Rosa Liksom",200)
lehti.tulosta_tiedot()
kirja.tulosta_tiedot()

#Tehtävä_2:
class Auto:
    def __init__(self,rekisteritunnus,huippunopeus,hetki_nopeus=0,kuljettu_matka=0):
        self.rekisteritunnus=rekisteritunnus
        self.huippunopeus=huippunopeus
        self.hetki_nopeus=hetki_nopeus
        self.kuljettu_matka=kuljettu_matka

    def nopeus(self,muuttos):
        self.hetki_nopeus=self.hetki_nopeus+muuttos
        return self.hetki_nopeus
    def matka(self,tunti):
        self.kuljettu_matka=self.kuljettu_matka+(self.hetki_nopeus*tunti)
        return self.kuljettu_matka
class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus,akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti=akkukapasiteetti
class Polttomoottoriauto(Auto):
    def __init__(self,rekisteritunnus, huippunopeus,bensatankin):
        super().__init__(rekisteritunnus,huippunopeus)
        self.bensatankin=bensatankin

sähkö=Sähköauto("ABC-15",180,52.5)
poltto=Polttomoottoriauto("ACD-123", 165, 32.3)
sähkö.nopeus(70)
sähkö.matka(3)
print(sähkö.kuljettu_matka)

poltto.nopeus(100)
poltto.matka(3)
print(poltto.kuljettu_matka)



        
    
        