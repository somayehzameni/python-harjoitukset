import json
from .clases import Alue ,Esine ,Erikoisesine,Pelaaja


def ohjeet():
    with open("pelin_paketti/ohjeet.txt","r") as f:
        tieto=f.read()
        print(tieto)
    
def kaivonporaustiimi():
        print("Kaivonporaustiimin puhelinnumero on: 0465892345")

def tallentaa_tilanne(metsä,aavikko,pelaaja,nykyinen_alue):
    nimi=pelaaja.nimi
    ikä=pelaaja.ikä
    
    metsä_lista=[]
    for esine in metsä.aluen_oletustyökalut:
        if hasattr(esine,"teho"):
            metsä_lista.append({"nimi":esine.nimi,"käyttö":esine.käyttö,"teho":esine.teho})
        else:
            metsä_lista.append({"nimi":esine.nimi,"käyttö":esine.käyttö})
    aavikko_lista=[]
    for esine in aavikko.aluen_oletustyökalut:
        if hasattr(esine,"teho"):
            aavikko_lista.append({"nimi":esine.nimi,"käyttö":esine.käyttö,"teho":esine.teho})
        else:
            aavikko_lista.append({"nimi":esine.nimi,"käyttö":esine.käyttö})
    repuu_lista=[]
    for esine in pelaaja.reppu:
        if hasattr(esine,"teho"):
            repuu_lista.append({"nimi":esine.nimi,"käyttö":esine.käyttö,"teho":esine.teho})
        else:
            repuu_lista.append({"nimi":esine.nimi,"käyttö":esine.käyttö})

    pelaajan_tiedot={"nimi":nimi,"ikä":ikä,"reppu_1":repuu_lista,"metsä_esine":metsä_lista,"aavikko_esine":aavikko_lista,"sijainti":nykyinen_alue}
    with open("tallennus.json","w") as f:
        json.dump(pelaajan_tiedot,f)
def load_tilanne():
    with open("tallennus.json","r") as f:
        data=json.load(f)
        print(data)
    reppun_lista=[]
    for esine in data["reppu_1"]:
        if "teho" in esine:
            uusi_esine=Erikoisesine(esine["nimi"],esine["käyttö"],esine["teho"])
        else:
           uusi_esine=Esine(esine["nimi"],esine["käyttö"]) 
        reppun_lista.append(uusi_esine)
    pelaaja=Pelaaja(data["nimi"],data["ikä"],reppun_lista)
    metsä_lista=[]
    for esine in data["metsä_esine"]:
        if "teho" in esine:
            usi_esine=Erikoisesine(esine["nimi"],esine["käyttö"],esine["teho"])
        else:
            uusi_esine=Esine(esine["nimi"],esine["käyttö"]) 
        metsä_lista.append(uusi_esine)
    metsä=Alue(data["sijainti"],"Tervetuloa metsään!\n\nMetsä on häätätilassa ja tarvitsee sinun apuaisi.\n\nTällä hetkellä on tapahtunut 2 suurta kriisiä metsässä:\n1:Laaja tulipalo pohjoisessa.\n2:Puiden laiton kaato",metsä_lista)
    aavikko_lista=[]
    for esine in data["aavikko_esine"]:
        if "teho" in esine:
            usi_esine=Erikoisesine(esine["nimi"],esine["käyttö"],esine["teho"])
        else:
            uusi_esine=Esine(esine["nimi"],esine["käyttö"]) 
        aavikko_lista.append(uusi_esine)
    aavikko=Alue(data["nimi"],"Tervetuloa aavikkoaluelle!\n\nTällä aluella on nyt kuivaa.Sinun pitää estää maaperän kuivuminen, muuten tämän alueen maaperän tuhoutuu.\n\nTällä hetkellä on 2 suurta ongelmaa aavikkoaluella:\n1:Vakava vesipula(Veden kaivot ja vesistöt ovat kuivuneet)\n2:maaperän kuivuminen ja pensaiden tuhoutunut.",aavikko_lista) 
    return pelaaja,metsä,aavikko,data["sijainti"]
def metsän_pelastus(metsä,aavikko,pelaaja):
    print()
    metsä.tiedot()
    print()
    valita=input("mitä kiirisiä valitset ensin?(1-2) ")
    print()
    if valita=="1":
        print("Metsässä on suuri tulipalo.Sinun tehtävä on samutttaa tulipaloa.\n\nMetsässä on seuraavat välineet: ")
        print()
        metsä.näyttä_aluen_esine()
        print()
        print("Mutta kuitenkin näiden esineiden teho on vähentynyt, koska ne ovat vanhoja. Jos kiiris in huomattavasti suuri, sinun kannattaa lisätä uusia esineita sinun reppuun. ")
        print()
        valinta_1=input("Tarvitsetko näitä esineitä vai haluatko uusia?(vanha/uusi)")
        print()
        if valinta_1=="vanha":
            komento_2=input("kirjoittaa esineen nimi")
            print()
            metsä.otta_esine_alueelta(komento_2,pelaaja)
            print()
            pelaaja.näyttä_esine()
            print()
            print("Palo on saatu hallintaan, mutta pelastusoperaatio ei ole vielä päättyneet")
            print()
        elif valinta_1=="uusi":
            print()
            työkalu=input("mitä työkalua sinä tarvitset? ")
            print()
            käyttö=input("Mihin käytät tätä työkalua?(vastaa vähintään kahdella sanalla)")
            print()
            teho=input("Syötä esineen teho(1-100)")
            print()
            uusi_esine=Erikoisesine(työkalu,käyttö,teho)
            print()
            pelaaja.lisää_esine_reppuun(uusi_esine)
            print()
            pelaaja.näyttä_esine()
            print()
            print("Palo sammutettiin ja sinä suoritit pelastusoperaatio onnistuneesti.")
            print()
        komento_5=input("Haluatko tallentaa pelin? yes/no")
        if komento_5=="yes":
            tallentaa_tilanne(metsä,aavikko,pelaaja,"metsä")
            print()
            print("Peli tallennettu!")
            print()
            return
        elif komento_5=="no":
            print("Peliä ei tallennettu")
            print()
        print("Palaat päävalikkoon")
        print()
        return
    elif valita=="2":
        print()
        print("Metsässä kaadetaan puita laittomasti.Sinun täytyy taistella tätä toimintaa vastaan.")
        print()
        print("Metsässä on seuraavat välineet:")
        print()
        metsä.näyttä_aluen_esine()
        print()
        valinta_3=input("Haluatko käyttää näitä esineitä vai tarvitsetko uusia esineitä? (vanha/uusi)")
        if valinta_3=="vanha":
            print()
            komento_4=input("kirjoittaa esineen nimi")
            print()
            metsä.otta_esine_alueelta(komento_4,pelaaja)
            print()
            pelaaja.näyttä_esine()
            print()
            print("sinä suoritit pelastusoperaatio mutta ei täydellisesti")
        elif valinta_3=="uusi":
            työkalu=input("mitä työkalua sinä tarvitset? ")
            print()
            käyttö=input("Mihin käytät tätä työkalua?(vastaa vähintään kahdella sanalla)")
            uusi_esine=Esine(työkalu,käyttö)
            print()
            pelaaja.lisää_esine_reppuun(uusi_esine)
            print()
            pelaaja.näyttä_esine()
            print("sinä suoritit pelastusoperaatio onnistuneesti")
            print()
        komento_5_2=input("Haluatko tallentaa pelin? yes/no")
        if komento_5_2=="yes":
            tallentaa_tilanne(metsä,aavikko,pelaaja,"metsä")
            print()
            print("Peli tallennettu!")
            print()
            return
        elif komento_5_2=="no":
            print("Peliä ei tallennettu")
            print()
        print("Palaat päävalikkoon")
        print()
        return   
def aavikon_etenemisen_estäminen(metsä,aavikko,pelaaja):
    print()
    aavikko.tiedot()
    print()
    valita=input("Mitä kriisiä valitset ensin?")
    print()
    if valita=="1":
        print ("Kaikki vesikaivot ovat kuivuneet.Sinun täytyy soittaa kaivonporaustiimiin.")
        print()
        kaivonporaustiimi()
        print()
        komento_6=input("Haluatko tallentaa pelin? yes/no")
        print()
        if komento_6=="yes":
            tallentaa_tilanne(metsä,aavikko,pelaaja,"aavikko")
            print()
            print("Peli tallennettu!")
            print()
            return
        elif komento_6=="no":
            print("Peliä ei tallennettu")
            print()
        print("Palaat päävalikkoon") 
        print()  
        return
    elif valita=="2":
       print()
       print("Maaperä on kuivunut ja pensaat on tuhoutunut") 
       print()
       print("Aavikossa on seuraavar välineet: ")
       print()
       aavikko.näyttä_aluen_esine()
       print()
       print("Mutta kuitenkin näiden esineiden teho on vähentynyt, koska ne ovat vanhoja. Jos kiiris in huomattavasti suuri, sinun kannattaa lisätä uusia esineita sinun reppuun. ")
       print()
       valinta_1=input("Tarvitsetko näitä esineitä vai haluatko uusia?(vanha/uusi)")
       print()
       if valinta_1=="vanha":
            komento_5=input("kirjoittaa esineen nimi")
            print()
            aavikko.otta_esine_alueelta(komento_5,pelaaja)
            print()
            pelaaja.näyttä_esine()
            print()
            print("sinä suoritit pelastusoperaatio mutta ei täydellisesti")
            print()
       elif valinta_1=="uusi":
           print()
           työkalu=input("mitä työkalua sinä tarvitset? ")
           print()
           käyttö=input("Mihin käytät tätä työkalua?(vastaa vähintään kahdella sanalla)")
           print()
           uusi_esine=Esine(työkalu,käyttö)
           print()
           pelaaja.lisää_esine_reppuun(uusi_esine)
           print()
           pelaaja.näyttä_esine()
           print()
           print("sinä suoritit pelastusoperaatio onnistuneesti")
           print()
       komento_6__2=input("Haluatko tallentaa pelin? yes/no")
       if komento_6__2=="yes":
            tallentaa_tilanne(metsä,aavikko,pelaaja,"aavikko")
            print("Peli tallennettu!")
            print()
            return
       elif komento_6__2=="no":
            print("Peliä ei tallennettu")
            print()
       print("Palaat päävalikkoon")
       print()
       return

def aloitta_peli():
    print()
    pelaajan_nimi=input("mitä sinun nimensi on? ")
    print()
    pelaajan_ikä=int(input("kuinka vanha olet? "))
    print()
    print(pelaajan_nimi,str(pelaajan_ikä))
    print()
    if pelaajan_ikä <12:
        print("Sinä olet alle 12-vuoitias")
        print()
    else :
        print("Tervetuloa peliin" , pelaajan_nimi)
        print()

        with open("pelin_paketti/intro.txt","r") as f:
            data=f.read()
            print(data)
            print()
    pelaaja=Pelaaja(pelaajan_nimi,pelaajan_ikä)
    esine_1_metsä=Esine("äämpäri","tulipalon sammuttamiseen")
    esine_2_metsä=Esine("kiikari","Puuvarkaiden havaitseminen")
    minun_lista_1=[]
    minun_lista_1.append(esine_1_metsä)
    minun_lista_1.append(esine_2_metsä)
    esine_1_aaviko=Esine("sadetin","kasvien kasteluun")
    minun_lista_2=[]
    minun_lista_2.append(esine_1_aaviko)
    metsä=Alue("metsä","Tervetuloa metsään!\n\nMetsä on häätätilassa ja tarvitsee sinun apuaisi.\n\nTällä hetkellä on tapahtunut 2 suurta kriisiä metsässä:\n\n1:Laaja tulipalo pohjoisessa.\n\n2:Puiden laiton kaato",minun_lista_1)
    aavikko=Alue("aavikko","Tervetuloa aavikkoaluelle!\n\nTällä aluella on nyt kuivaa.Sinun pitää estää maaperän kuivuminen, muuten tämän alueen maaperän tuhoutuu.\n\nTällä hetkellä on 2 suurta ongelmaa aavikkoaluella:\n\n1:Vakava vesipula(Veden kaivot ja vesistöt ovat kuivuneet)\n\n2:maaperän kuivuminen ja pensaiden tuhoutunut.",minun_lista_2)   
    alue_1="Metsäkato-kriisi"
    alue_2="Aavikoituma-kriisi"
    print()
    komento=input("Valitse alue_1 tai alue_2")
    print()
    if komento=="alue_1":
        metsän_pelastus(metsä,aavikko,pelaaja)
    elif komento=="alue_2":
        aavikon_etenemisen_estäminen(metsä,aavikko,pelaaja)

def päävalikko_1():
    
    päävaliko_1="aloita peli"
    päävalikko_2="lataa peli"
    päävaliko_3="ohjeet"
    päävaliko_q="lopetttaa"
    print("Päävalikko")
    print("1:" ,päävaliko_1)
    print("2:" ,päävalikko_2)
    print("3:",päävaliko_3)
    print("q:" ,päävaliko_q)
    print()
    päävalikko=input("Valitse komento(1-3,q): ")
    print()
    while True:
        print("Päävalikko")
        print("1:" ,päävaliko_1)
        print("2:" ,päävalikko_2)
        print("3:",päävaliko_3)
        print("q:" ,päävaliko_q)
        päävalikko=input("Valitse komento(1-3,q): ")
        if päävalikko=="1":
            aloitta_peli()
        elif päävalikko=="2":
            pelaaja,metsä,aavikko,sijainti=load_tilanne()
            if sijainti=="metsä":
               metsän_pelastus(metsä,aavikko,pelaaja)
            elif sijainti=="aavikko":
               aavikon_etenemisen_estäminen(metsä,aavikko,pelaaja)
        elif päävalikko=="3":
            ohjeet()
        elif päävalikko=="q" :
            print("lopettaa,kiitos pelaamisesta")
            break     
        



    

   