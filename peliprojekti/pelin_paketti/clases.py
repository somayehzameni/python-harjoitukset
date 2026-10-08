#Kaikki classes ovat tällä.
class Esine:
    def __init__(self,nimi,käyttö):
        self.nimi=nimi
        self.käyttö=käyttö
    def __str__(self) :
        return f"nimi: {self.nimi} | käyttö: {self.käyttö}"  
class Erikoisesine(Esine):
    def __init__(self,nimi,käyttö,teho):
        super().__init__(nimi,käyttö)
        self.teho=teho
    def __str__(self):
        return f"{super().__str__()} | teho: {self.teho}"
class Alue():
    def __init__(self,nimi,kuvaus,aluen_oletustyökalut):
        self.nimi=nimi
        self.kuvaus=kuvaus
        self.aluen_oletustyökalut=aluen_oletustyökalut
    def tiedot(self):
        print(f"{self.kuvaus}")
    def näyttä_aluen_esine(self):
        for i in self.aluen_oletustyökalut:
            print(i)
    def otta_esine_alueelta(self,esine,pelaaja):
        for i in self.aluen_oletustyökalut:
            if esine==i.nimi:
               self.aluen_oletustyökalut.remove(i)
               print(f"{i.nimi} otettiin alueelta")
               pelaaja.lisää_esine_reppuun(i)

    def lisää_esine_alueen(self,esine,pelaaja):
        poistetuu_esine=pelaaja.remove_esine_repusta(esine)
        if poistetuu_esine is not None:
            self.aluen_oletustyökalut.append(poistetuu_esine)
            print("lisätään esineen alueen")
        else:
            self.aluen_oletustyökalut.append(esine)
            print("lisäätään")
class Pelaaja():
    def __init__(self,nimi,ikä,reppu=[]):
        self.nimi=nimi
        self.ikä=ikä
        self.reppu=reppu
    def lisää_esine_reppuun(self,esine):
        self.reppu.append(esine)
    def remove_esine_repusta(self,esine):
        for i in self.reppu:
            if i.nimi==esine:
                self.reppu.remove(i)
                return i
    def näyttä_esine(self):
        for i in self.reppu:
            print(i)

