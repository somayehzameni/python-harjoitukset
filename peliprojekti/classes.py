#Kaikki classes ovat tällä.
class Alue:
    def __init__(self,nimi,kuvaus):
        self.nimi=nimi
        self.kuvaus=kuvaus
    def tiedot(self):
        print(f"{self.kuvaus}")

class Esine:
    def __init__(self,nimi,käyttö):
        self.nimi=nimi
        self.käyttö=käyttö
    def tiedot_1(self):
        print(f"{self.nimi} , {self.käyttö}")

class Pelaaja:
    def __init__(self,nimi,ikä,sijainti=None,reppu=[]):
        self.nimi=nimi
        self.ikä=ikä
        self.sijainti=sijainti
        self.reppu=reppu
    def lisää_esineet(self,työkalu):
        self.reppu.append(työkalu)
    def näyttä_esineet(self):
        if len(self.reppu)!=0:
            for item in self.reppu:
                item.tiedot_1()
        else:
            print("reppu on tyhjä!!")


